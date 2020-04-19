/*
 This file contains a bunch of utility functions for manipulating Watson Conversation Service files
*/

'use strict';
let fs = require('fs');
let csv = require('fast-csv');
let path = require('path');
let del = require('del');

let watson_conversation_utils = {};


watson_conversation_utils.setCloudFunctionName = function (watsonWorkspace, cloudFunction) {
    const nodes = watsonWorkspace.dialog_nodes.filter(node => node.actions && node.actions.length > 0);

    for (const node of nodes) {
        for (const action of node.actions) {
            action.name = action.name.replace(cloudFunction.replace, cloudFunction.with);
        }
    }
}
watson_conversation_utils.setDaimlerLookupTableDataParameters = function (watsonWorkspace, actionName, parameters) {
    const nodes = watsonWorkspace.dialog_nodes.filter(node => node.actions && node.actions.length > 0);

    for (const node of nodes) {
        for (const action of node.actions) {
            if (action.name == actionName) {
                for (const parameter in parameters) {
                    action.parameters.data[parameter] = parameters[parameter];
                }
            }
        }
    }
}


watson_conversation_utils.setCloudFunctionCredentials = function (workspace, credentialsKey) {

    const nodeToChangeContext = "Welcome";

    let dialog_nodes = workspace.dialog_nodes;

    let dialogNode = dialog_nodes.find(
        node => node.dialog_node === nodeToChangeContext
    );
    if (!dialogNode) {
        console.error(`${nodeToChangeContext} is not in the workspace`);
        exit(1);
    }


    let credentials = credentialsKey.split(":");

    dialogNode.context.private.credentials.user = credentials[0];
    dialogNode.context.private.credentials.password = credentials[1];


}


watson_conversation_utils.setBotName = function (workspace, bot_name) {

    const nodeToChangeContext = "Welcome";
    const contextVariable = "bot_name";

    let dialog_nodes = workspace.dialog_nodes;

    let dialogNode = dialog_nodes.find(
        node => node.dialog_node === nodeToChangeContext
    );
    if (!dialogNode) {
        console.error(`${nodeToChangeContext} is not in the workspace`);
        exit(1);
    }
    if (!dialogNode.context[contextVariable]) {
        console.error(`${contextVariable} is not in the Welcome dialog`);
        exit(1);
    }

    dialogNode.context[contextVariable] = dialogNode.context[contextVariable].replace(bot_name.replace, bot_name.with);
}

watson_conversation_utils.extractWorkspaceFromFiles = function (inputDirectory) {
    const metadataFileName = "metadata.json";

    const subDirectoryNodes = "nodes";
    const subDirectoryIntents = "intents";

    const subDirectoryEntities = "entities"




    //readMetadata

    var workspace = JSON.parse(
        fs.readFileSync(`${inputDirectory}${metadataFileName}`, "utf8")
    );

    let nodes = [];

    fs.readdirSync(`${inputDirectory}${subDirectoryNodes}`).forEach(file => {
        let path = `${inputDirectory}${subDirectoryNodes}/${file}`;

        var node = JSON.parse(fs.readFileSync(path, "utf8"));
        nodes.push(node);
    });

    workspace["dialog_nodes"] = nodes;

    let intents = [];

    fs.readdirSync(`${inputDirectory}${subDirectoryIntents}`).forEach(file => {
        let path = `${inputDirectory}${subDirectoryIntents}/${file}`;

        var intent = JSON.parse(fs.readFileSync(path, "utf8"));
        intents.push(intent);
    });

    workspace["intents"] = intents;


    let entities = [];

    fs.readdirSync(`${inputDirectory}${subDirectoryEntities}`).forEach(file => {
        let path = `${inputDirectory}${subDirectoryEntities}/${file}`;

        var entity = JSON.parse(fs.readFileSync(path, "utf8"));
        entities.push(entity);
    });

    workspace["entities"] = entities;

    return workspace;
}


watson_conversation_utils.extractMetadataFromJSON = function (json) {

    let res = {};
    for (let property in json) {
        if (property != 'entities' && property != 'intents' && property != 'dialog_nodes') {
            res[property] = json[property];
        }
    }

    return res;
}

//extracts the answers in an array of nodes
watson_conversation_utils.extractNodesFromJSON = function (json) {
    let nodeArray = new Array();
    let nodeMap = new Map();
    let nodes = json.dialog_nodes;

    function compare(a, b) {
        if (a.dialog_node < b.dialog_node)
            return -1;
        if (a.dialog_node > b.dialog_node)
            return 1;
        return 0;
    }

    // create a node array
    for (let node of nodes) {
        nodeArray.push(node);
        nodeMap.set(node.dialog_node, node);
    }

    let nodeArraySorted = nodeArray.sort(compare);

    return nodeArraySorted;
}

watson_conversation_utils.checkNodeConsistency = function (json) {
    let nodeArray = new Array();
    let nodeMap = new Map();
    let nodes = json.dialog_nodes;


    // create a node array
    for (let node of nodes) {
        nodeArray.push(node);
        nodeMap.set(node.dialog_node, node);
    }


    for (let node of nodes) {
        let parent = node.parent;
        if (parent !== undefined) {
            let parentNode = nodeMap.get(parent);
            if (parentNode === undefined) {
                console.log("Node ID=" + node.dialog_node + " could not find parent ID=" + parent);
            }
        }

        let sibling = node.previous_sibling;

        if (sibling !== undefined) {
            let siblingNode = nodeMap.get(sibling);
            if (siblingNode === undefined) {
                console.log("Node ID=" + node.dialog_node + " could not find sibling ID=" + sibling);
            }
        }

    }

}


//extracts a map of the nodes
watson_conversation_utils.extractNodeMapFromJSON = function (json) {
    let nodeMap = new Map();
    let nodes = json.dialog_nodes;

    // create a node array
    for (let node of nodes) {

        nodeMap.set(node.dialog_node, node);
    }
    return nodeMap;
}





//extracts the answers in an array of arrays: [ [answerId, answer_text,attachment_id,node_id, node_title, parent_node_id, parent_node_title],[...]]
// TODO optize this - there is lots of duplicated code
watson_conversation_utils.extractAnswersFromJSON = function (json, paramOptions) {


    let options = {
        replaceWithAnswerIds: false
    }

    if (paramOptions.replaceWithAnswerIds) {
        options.replaceWithAnswerIds = paramOptions.replaceWithAnswerIds;
    }


    let answerArray = new Array();
    let attachmentArray = new Array();
    let nodeMap = new Map();
    let nodes = json.dialog_nodes;

    // create a node map
    for (let node of nodes) {
        let nodeId = node.dialog_node;
        nodeMap.set(nodeId, node);
    }

    let aId = 1;

    function getAnswer(answerId, textAnswer, attachmentIds, nodeId, nodeTitle, parentId, parentTitle, voiceAnswer) {
        return { answerId: answerId, answer: textAnswer, attachmentIds: attachmentIds, nodeId: nodeId, nodeTitle: nodeTitle, parentId: parentId, parentTitle: parentTitle, voice: voiceAnswer };
    }

    for (let node of nodes) {



        let nodeId = node.dialog_node;
        let nodeTitle = node.title;
        if (nodeTitle == null) {
            nodeTitle = '';
        }
        let parentId = node.parent;
        let parentTitle = ''

        if (parentId == null) {
            parentId = '';
        } else {
            let parent = nodeMap.get(parentId);
            if (parent === undefined) {
                console.log(parentId);
            }

            parentTitle = parent.title ? nodeMap.get(parentId).title : '';
        }


        // There are three possibilities for text answer syntax!!! :-(
        if (node.output && node.output.text) {
            let outputText = node.output.text;
            let attachmentIds = "";
            let textAnswer = "";
            let voiceAnswer = "";
            /*
                "output": {
                    "text": "Hast du ein Problem mit dem Konfigurator, der Website oder etwas anderem?"

                  }

             */
            if (typeof outputText === 'string') {
                let answerId = aId + '_' + nodeId + '_' + nodeTitle + '_1';
                let atts = this.parseAnswer(outputText);

                if (atts.attachments !== undefined) {
                    for (let a of atts.attachments) {
                        let attachmentId = attachmentArray.length + 1 + '_' + nodeId + '_' + nodeTitle;
                        let attachment = { id: attachmentId, attachment: a };
                        attachmentArray.push(attachment);
                        attachmentIds += attachmentId + '\n';
                    }
                }
                if (options.replaceWithAnswerIds) {
                    node.output.text = answerId;
                }
                if (atts.answer.search("<speak>") < 0) {
                    textAnswer = atts.answer;
                }
                if (atts.answer.search("<speak>") >= 0) {
                    voiceAnswer = atts.answer;
                }

                let answer = getAnswer(answerId, textAnswer, attachmentIds, nodeId, nodeTitle, parentId, parentTitle, voiceAnswer);
                answerArray.push(answer);
                aId += 1;

                /*
                "output": {
                    "text": {
                      "values": [
                        "Hast du ein Problem mit dem Konfigurator, der Website oder etwas anderem?"
                      ],
                      "selection_policy": "sequential"
                    }
                  }
                 */


            } else if (typeof outputText === 'object' && outputText.values) {
                //pick the first voice answer from the array
                let firstVoiceAnswer = outputText.values.find(function (answer) {
                    return answer.search("<speak>") >= 0;
                });
                if (firstVoiceAnswer !== undefined) {
                    firstVoiceAnswer = this.parseAnswer(firstVoiceAnswer).answer;
                } else {
                    firstVoiceAnswer = "";
                }
                //pick the first text answer from the array
                let firstTextAnswer = outputText.values.find(function (answer) {
                    return answer.search("<speak>") < 0;
                });
                if (firstTextAnswer !== undefined) {
                    firstTextAnswer = this.parseAnswer(firstTextAnswer).answer;
                } else {
                    firstTextAnswer = "";
                }


                let textAnswer = firstTextAnswer;
                let voiceAnswer = firstVoiceAnswer;
                let nodeNumber = 0;
                //iterate answer variations
                for (let i = 0; i < outputText.values.length; i++) {

                    let text = outputText.values[i];
                    let attachmentIds = "";
                    let answerId = aId + '_' + nodeId + '_' + nodeTitle + '_' + (nodeNumber + 1);
                    if (text !== undefined) {
                        let atts = this.parseAnswer(text);
                        if (atts.attachments !== undefined) {
                            for (let a of atts.attachments) {
                                let attachmentId = attachmentArray.length + 1 + '_' + nodeId + '_' + nodeTitle;
                                let attachment = { id: attachmentId, attachment: a };
                                attachmentArray.push(attachment);
                                attachmentIds += attachmentId + '\n';
                            }
                        }
                        if (options.replaceWithAnswerIds) {
                            outputText.values[i] = answerId;
                        }

                        if (atts.answer.search("<speak>") >= 0) {
                            voiceAnswer = atts.answer;
                        }
                        if (atts.answer.search("<speak>") < 0) {
                            textAnswer = atts.answer;
                        }
                        if (firstTextAnswer.length === 0) {
                            textAnswer = voiceAnswer;
                        }



                        if (!(i == 0 && outputText.values.length > 1 && textAnswer == firstTextAnswer && voiceAnswer == firstVoiceAnswer) || (firstTextAnswer.length == 0 || firstVoiceAnswer.length == 0)) {
                            let answer = getAnswer(answerId, textAnswer, attachmentIds, nodeId, nodeTitle, parentId, parentTitle, voiceAnswer);
                            answerArray.push(answer);
                            aId += 1;
                            nodeNumber++;
                        }
                    }
                }
            }

            /*
              "output": {
                    "generic": [
                      {
                        "values": [
                          {
                            "text": "Hier kannst Du Dir die Preisliste für den smart $last_model_discussed  anschauen.  {   \"type\":\"links\",\"links\": [  {\"title\":\"Hier anklicken\",\"url\":\"https://www.smart.com/de/de/index/downloadcenter.html\"}  ] }"
                          }
                        ],
                        "response_type": "text",
                        "selection_policy": "multiline"
                      },
                      {
                        "values": [
                          {
                            "text": "Sofern preislich was für Dich dabei ist kannst Du auch gerne direkt ins Detail gehen und Dir Dein Auto konfigurieren :) Hast Du Lust?  {   \"type\":\"multichoice\",    \"options\": [        {\"label\":\"ja\",\"value\":\"ja\"},  {\"label\":\"nein\",\"value\":\"nein\"}  ] }"
                          }
                        ],
                        "response_type": "text",
                        "selection_policy": "multiline"
                      }
                    ]
                  },
             */
        } else if (node.output && node.output.generic) {

            // iterate answers
            for (let j = 0; j < node.output.generic.length; j++) {

                // iterate answer variations
                let answers = node.output.generic[j].values;

                //pick the first text answer from the array
                let firstTextAnswer = "";
                let firstVoiceAnswer = "";
                answers.find(function (answer) {
                    if (answer.text.includes("<speak>")) {
                        firstVoiceAnswer = answer.text;
                    }
                    if (!answer.text.includes("<speak>")) {
                        firstTextAnswer = answer.text;
                    }
                });

                if (firstVoiceAnswer !== undefined && firstVoiceAnswer.length !== 0) {
                    firstVoiceAnswer = this.parseAnswer(firstVoiceAnswer).answer;
                }
                if (firstTextAnswer !== undefined && firstTextAnswer.length !== 0) {
                    firstTextAnswer = this.parseAnswer(firstTextAnswer).answer;
                }

                let textAnswer = firstTextAnswer;
                let voiceAnswer = firstVoiceAnswer;
                let nodeNumber = 0;

                for (let i = 0; i < answers.length; i++) {
                    let text = answers[i].text;
                    let answerId = aId + '_' + nodeId + '_' + nodeTitle + '_' + (j + 1) + '_' + (nodeNumber + 1);

                    let attachmentIds = '';

                    if (text !== undefined) {
                        let atts = this.parseAnswer(text);
                        if (atts.attachments !== undefined) {
                            for (let a of atts.attachments) {
                                let attachmentId = attachmentArray.length + 1 + '_' + nodeId + '_' + nodeTitle;
                                let attachment = { id: attachmentId, attachment: a };
                                attachmentArray.push(attachment);
                                attachmentIds += attachmentId + '\n';
                            }
                        }

                        if (options.replaceWithAnswerIds) {
                            answers[i].text = answerId;
                        }

                        if (atts.answer.search("<speak>") >= 0) {
                            voiceAnswer = atts.answer;
                        }
                        if (atts.answer.search("<speak>") < 0) {
                            textAnswer = atts.answer;
                        }
                        if (firstTextAnswer.length === 0) {
                            textAnswer = voiceAnswer;
                        }

                        if (!(i == 0 && answers.length > 1 && textAnswer == firstTextAnswer && voiceAnswer == firstVoiceAnswer) || (firstTextAnswer.length == 0 || firstVoiceAnswer.length == 0)) {
                            let answer = getAnswer(answerId, textAnswer, attachmentIds, nodeId, nodeTitle, parentId, parentTitle, voiceAnswer);
                            answerArray.push(answer);
                            aId += 1;
                            nodeNumber++;
                        }
                    }



                }
            }
        }
    }
    return { answers: answerArray, attachments: attachmentArray, json: json };
};

watson_conversation_utils.extractIntentsFromJSON = function (json) {
    // calculate the answers
    let intentMap = new Map();
    let intents = json.intents;
    for (let intent of intents) {

        let intentTitle = intent.intent;
        let intentExamples = Array();

        for (let example of intent.examples) {
            intentExamples.push(example.text);
        }

        intentMap.set(intentTitle, intentExamples);

    }
    return intentMap;
};


watson_conversation_utils.extractEntitiesFromJSONToObjectArray = function (json) {

    let entityArray = [];
    let entities = json.entities;
    for (let entity of entities) {
        entityArray.push(entity);


    }
    return entityArray;
};


watson_conversation_utils.extractEntitiesFromJSON = function (json) {

    let entityMap = new Map();
    let entities = json.entities;
    for (let entity of entities) {

        let entityTitle = entity.entity.toLowerCase();

        let valuesMap = new Map();
        for (let value of entity.values) {
            let valueTitle = value.value.toLowerCase();
            if (value.type === 'synonyms') {
                let valueSynonyms = Array();
                for (let syn of value.synonyms) {
                    valueSynonyms.push(syn);
                }
                valuesMap.set(valueTitle, valueSynonyms)
            } else if (value.type === 'patterns') {
                let valuePatterns = Array();
                for (let pattern of value.patterns) {
                    valuePatterns.push(pattern);
                }
                valuesMap.set(valueTitle, valuePatterns)
            }


        }

        entityMap.set(entityTitle, valuesMap);

    }
    return entityMap;
};


watson_conversation_utils.writeAnswersToJSON = function (answersArray, outputJSONFilePath) {
    this.writeObjectToJSONFile(answersArray, outputJSONFilePath);
};


watson_conversation_utils.writeAnswersToCSV = function (answersArray, outputCSVFilePath) {
    let csvStream = this.createCSVWriteStream(outputCSVFilePath);

    function compare(a, b) {
        if (a.answerId < b.answerId)
            return -1;
        if (a.answerId > b.answerId)
            return 1;
        return 0;
    }

    let sortedAnswersArray = Array.from(answersArray).sort(compare); // sort keys so that intents are written alphabetically sorted

    csvStream.write({ answerId: "id", answer_text: "text", attachment_id: "attachment_id", node_id: "node_id", node_title: "node_title", parent_node_id: "parent_node_id", parent_node_title: "parent_node_title" });

    for (const answer of sortedAnswersArray) { //[ answerId, answer_text,attachment_id,node_id, node_title, parent_node_id, parent_node_title]
        let answerId = answer.answerId;
        let answerText = answer.answer;
        let attachmentId = answer.attachmentIds;
        let answerNodeId = answer.nodeId;
        let answerNodeTitle = answer.nodeTitle;
        let answerParentId = answer.parentId;
        let answerParentTitle = answer.parentTitle;
        csvStream.write({
            answerId: answerId,
            answer_text: answerText.replace(/\n/g, "<br />"),
            attachment_id: attachmentId,
            node_id: answerNodeId,
            node_title: answerNodeTitle,
            parent_node_id: answerParentId,
            parent_node_title: answerParentTitle
        });
    }

    csvStream.end();
};

watson_conversation_utils.writeIntentsToCSV = function (intentsMap, outputCSVFilePath) {
    let csvStream = this.createCSVWriteStream(outputCSVFilePath);
    let keys = Array.from(intentsMap.keys()).sort(); // sort keys so that intents are written alphabetically sorted
    for (const intent of keys) {
        let exampleArray = intentsMap.get(intent);
        for (const example of exampleArray) {
            csvStream.write({ intent: intent, example: example });
        }
    }

    csvStream.end();
};

watson_conversation_utils.createCSVWriteStream = function (csvFilePath) {
    let csvStream = csv.createWriteStream({ headers: false });
    let writableStream = fs.createWriteStream(csvFilePath);
    writableStream.on("finish", function () {

    });

    csvStream.pipe(writableStream);
    return csvStream;
}

watson_conversation_utils.writeMetadataToJSON = function (metadata, jsonFilePath) {
    this.writeObjectToJSONFile(metadata, jsonFilePath);
}



watson_conversation_utils.writeEntitiesToCSV = function (entitiesMap, outputCSVFilePath) {
    let csvStream = this.createCSVWriteStream(outputCSVFilePath);
    let keys = Array.from(entitiesMap.keys()).sort();

    for (const entity of keys) {
        let entityTitle = entity;
        let valueMap = entitiesMap.get(entity);
        for (const value of valueMap.entries()) {
            let key = value[0];
            let synonymsOrPatterns = value[1];
            csvStream.write({ title: entityTitle, syns: synonymsOrPatterns });
        }
    }

    csvStream.end();
};

watson_conversation_utils.writeNodesToDir = function (nodes, outputDirectory) {

    for (const node of nodes) {
        let nodeId = node.dialog_node;
        let parentId = node.parent;
        watson_conversation_utils.writeObjectToJSONFile(node, outputDirectory + '/parent_' + parentId + '_' + nodeId + '.json');
    }



}

watson_conversation_utils.cleanDir = function (directory) {
    del.sync([directory + '/*.*']);
}

watson_conversation_utils.createOrCleanDir = function (dir) {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir); else this.cleanDir(dir);
}

watson_conversation_utils.createDir = function (dir) {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);
}


watson_conversation_utils.writeIntentsEntitiesAnswersToFiles = function (metadataObject, intentsMap, entityArray, answersArray, nodeArray, outputDirectory) {
    let outDir = outputDirectory;
    let intentsDir = outputDirectory + '/intents';
    let entitiesDir = outputDirectory + '/entities';
    let answersDir = outputDirectory + '/answers';
    let nodesDir = outputDirectory + '/nodes';
    this.createOrCleanDir(outDir);
    this.createOrCleanDir(intentsDir);
    this.createOrCleanDir(entitiesDir);
    this.createOrCleanDir(answersDir);
    this.createOrCleanDir(nodesDir);

    //one file for metadata
    this.writeMetadataToJSON(metadataObject, outputDirectory + '/metadata.json')

    //one file per intent
    let keys = Array.from(intentsMap.keys()).sort(); // sort keys so that intents are written alphabetically sorted
    for (const intent of keys) {
        let exampleArray = intentsMap.get(intent).sort();
        let exampleObjArray = [];
        for (let ex of exampleArray) {
            exampleObjArray.push({ text: ex });
        }
        let intentObject = { intent: intent, examples: exampleObjArray };
        //this.writeJSONtoFile(intentObject,intentsDir +'/' + intent + '.json');
        this.writeObjectToJSONFile(intentObject, intentsDir + '/' + intent + '.json')
    }


    // one file for all entities
    for (const entity of entityArray) {
        this.writeObjectToJSONFile(entity, entitiesDir + "/" + entity.entity + ".json");
    }
    // one file for all answers
    this.writeAnswersToJSON(answersArray, answersDir + '/answers.json');

    // one file per node
    this.writeNodesToDir(nodeArray, nodesDir);
}

watson_conversation_utils.loadAnswersFromCSV = function (answersCSV, options, callback) {
    let answersMap = new Map();
    let stream = fs.createReadStream(answersCSV, options);
    let csvStream = csv()
        .on("data", function (data) {
            answersMap.set(data[0], data[1]);
        })
        .on("end", function () {
            callback(answersMap);
        });

    stream.pipe(csvStream);

}

watson_conversation_utils.writeObjectToJSONFile = function (sourceJSON, targetJSONFile) {
    let outJson = JSON.stringify(sourceJSON, null, 4);
    fs.writeFile(targetJSONFile, outJson, 'utf8', function (err) {
        if (err) throw err;
    });
}



watson_conversation_utils.replaceAnswersInWorkspace = function (modeCodes, answersMap, sourceJSON) {

    let nodes = sourceJSON.dialog_nodes;
    for (let node of nodes) {
        let nodeTitle = node.title;
        let outputText = node.output.text;
        if (outputText === undefined) {
            outputText = { values: [], selection_policy: "random" };
            node.output.text = outputText;
        }
        outputText.values = [];
        outputText.selection_policy = "random";
        let i = 1;
        let out = false;
        while (!out) {
            let code = nodeTitle + '_' + i;
            let text = answersMap.get(code);
            if (text === undefined) {
                out = true;
            } else {
                if (modeCodes) {
                    outputText.values.push(code);
                } else {
                    outputText.values.push(text);
                }

                i++;
            }
        }
    }

    return sourceJSON;
}


function parseAttachmentsWithRegex(regexExpr, text) {
    let regex = new RegExp(regexExpr, "g");
    let matches = [];
    let match;
    while (match = regex.exec(text)) {
        matches.push(JSON.parse(match[0]));
    }

    return matches;
}

function extractTextAnswer(text) {
    let res = text;
    let i = text.search("{");
    if (i >= 0) {
        res = text.substring(0, i);
    }
    if (res.length == 0) {
        let speakStartPos = text.search("<speak>");
        let speakEndPos = text.search("</speak>");
        if (speakStartPos >= 0) {
            res = text.substring(speakStartPos, speakEndPos + 8);
        } else {
            let obj = JSON.parse(text);
            switch (obj.type) {
                case "multichoice":
                    res = "";
                    break;
                case "links":
                    res = "";
                    break;
                case "hints":
                    res = "";
                    break;
                case "text":
                    res = obj.text;
                default:
                    res = "XXXXX";
            }
        }
    }
    return res;
}

watson_conversation_utils.parseAnswer = function (answer) {
    let resAttachments = [];
    let resAnswer = '';
    let sp = '[ |\t|\r|\n]*';
    let value = '[^"{}]*';
    //let regexGroups = {answer: 1, attachments : 2};
    let multiChoiceRegex = `{${sp}"type"${sp}:${sp}"multichoice"${sp},${sp}"options"${sp}:${sp}\\[.*\\]${sp}}`;
    let hintsRegex = `{${sp}"type"${sp}:${sp}"hints"${sp},${sp}"options"${sp}:${sp}\\[.*\\]${sp}}`;
    let imageRegex = `{${sp}"type"${sp}:"image"${sp},${sp}"title"${sp}:${sp}"${value}"${sp},${sp}"thumbnail_filename"${sp}:${sp}"${value}"${sp},${sp}"file"${sp}:${sp}"${value}"${sp}}`;
    let videoRegex = `{${sp}"type"${sp}:"video"${sp},${sp}"title"${sp}:${sp}"${value}"${sp},${sp}"thumbnail_filename"${sp}:${sp}"${value}"${sp},${sp}"file"${sp}:${sp}"${value}"${sp}}`;
    let youtubeRegex = `{${sp}"type"${sp}:${sp}"youtube"${sp},${sp}"title"${sp}:${sp}"${value}"${sp},${sp}"thumbnail_filename"${sp}:${sp}"${value}"${sp},${sp}"youtube_id"${sp}:${sp}"${value}"${sp}}`;
    let linksRegex = `{${sp}"type"${sp}:${sp}"links"${sp},${sp}"links"${sp}:${sp}\\[${sp}.*${sp}\\]${sp}}`;
    let answerRegex = '.+(?![^{}])';

    let regexes = [multiChoiceRegex, hintsRegex, imageRegex, videoRegex, youtubeRegex, linksRegex];
    for (let regex of regexes) {
        resAttachments = parseAttachmentsWithRegex(regex, answer);
        if (resAttachments.length > 0) {
            break;
        }
    }

    resAnswer = extractTextAnswer(answer);

    return { answer: resAnswer, attachments: resAttachments };
}


module.exports = watson_conversation_utils;






