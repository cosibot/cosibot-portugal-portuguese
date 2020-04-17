/*
 This file contains a bunch of utility functions for manipulating Watson Conversation Service files
*/

'use strict';
let fs = require('fs');
let csv = require('fast-csv');
let path = require('path');
let del = require('del');
const yaml = require('yaml')
let rasa_utils = {};


rasa_utils.extractIntentsFromJSON = function (json) {
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


rasa_utils.extractMetadataFromJSON = function (json) {

    let res = {};
    for (let property in json) {
        if (property != 'entities' && property != 'intents' && property != 'dialog_nodes') {
            res[property] = json[property];
        }
    }

    return res;
}

rasa_utils.extractAnswersFromJSON = function (json) {

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
            if (typeof outputText === 'string') {
                let answer =  JSON.parse(outputText);
                answerArray.push({title: nodeTitle , answer: answer});
                aId += 1;

            } else if (typeof outputText === 'object' && outputText.values) {

                //iterate answer variations
                for (let i = 0; i < outputText.values.length; i++) {

                    let text = outputText.values[i];
                    let answer =  JSON.parse(text);
                    answerArray.push({title: nodeTitle , answer: answer});
                }
            }

        } else if (node.output && node.output.generic) {

            // iterate answers
            for (let j = 0; j < node.output.generic.length; j++) {

                // iterate answer variations
                let answers = node.output.generic[j].values;

                for (let i = 0; i < answers.length; i++) {
                    let text = answers[i].text;
                    let answer =  JSON.parse(text);
                    answerArray.push({title: nodeTitle , answer: answer});
                }
            }
        }
    }
    return { answers: answerArray };
};



rasa_utils.writeAnswersToJSON = function (answersArray, outputJSONFilePath) {
    this.writeObjectToJSONFile(answersArray, outputJSONFilePath);
};


rasa_utils.writeAnswersToCSV = function (answersArray, outputCSVFilePath) {
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

rasa_utils.writeIntentsToCSV = function (intentsMap, outputCSVFilePath) {
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

rasa_utils.createCSVWriteStream = function (csvFilePath) {
    let csvStream = csv.createWriteStream({ headers: false });
    let writableStream = fs.createWriteStream(csvFilePath);
    writableStream.on("finish", function () {

    });

    csvStream.pipe(writableStream);
    return csvStream;
}

rasa_utils.writeMetadataToJSON = function (metadata, jsonFilePath) {
    this.writeObjectToJSONFile(metadata, jsonFilePath);
}



rasa_utils.writeEntitiesToCSV = function (entitiesMap, outputCSVFilePath) {
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

rasa_utils.writeNodesToDir = function (nodes, outputDirectory) {

    for (const node of nodes) {
        let nodeId = node.dialog_node;
        let parentId = node.parent;
        rasa_utils.writeObjectToJSONFile(node, outputDirectory + '/parent_' + parentId + '_' + nodeId + '.json');
    }



}

rasa_utils.cleanDir = function (directory) {
    del.sync([directory + '/*.*']);
}

rasa_utils.createOrCleanDir = function (dir) {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir); else this.cleanDir(dir);
}

rasa_utils.createDir = function (dir) {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);
}


rasa_utils.writeIntentsEntitiesAnswersToFiles = function (metadataObject, intentsMap, entityArray, answersArray, nodeArray, outputDirectory) {
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

    //build the nlu.md
    let nlu ='';
    let keys = Array.from(intentsMap.keys()).sort(); // sort keys so that intents are written alphabetically sorted
    for (const intent of keys) {
        let intentTitle = '## intent:' + intent + '\n';
        let exampleArray = intentsMap.get(intent).sort();
        let exampleList = yaml.stringify(exampleArray);

        nlu += intentTitle + exampleList + '\n';
    }

    this.writeStringToFile(nlu,intentsDir + '/nlu.md');


    // one file for all entities
    //for (const entity of entityArray) {
      //  this.writeObjectToJSONFile(entity, entitiesDir + "/" + entity.entity + ".json");
    //}


    // one file for all answers
    this.writeAnswersToJSON(answersArray, answersDir + '/answers.json');

    // one file per node
    //this.writeNodesToDir(nodeArray, nodesDir);
}



rasa_utils.writeObjectToJSONFile = function (sourceJSON, targetJSONFile) {
    let outJson = JSON.stringify(sourceJSON, null, 4);
    fs.writeFile(targetJSONFile, outJson, 'utf8', function (err) {
        if (err) throw err;
    });
}

rasa_utils.writeStringToFile = function (string, targetFile) {
    fs.writeFile(targetFile, string, 'utf8', function (err) {
        if (err) throw err;
    });
}






module.exports = rasa_utils;






