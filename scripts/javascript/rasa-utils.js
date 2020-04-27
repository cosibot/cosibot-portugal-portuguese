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

        intentMap.set(intentTitle.toLowerCase(), intentExamples);

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
        let parentTitle = '';

        if (parentId == null) {
            parentId = '';
        } else {
            let parent = nodeMap.get(parentId);
            if (parent === undefined) {
                console.log(parentId);
            }

            parentTitle = parent.title ? nodeMap.get(parentId).title : '';
        }


        if (node.output && node.output.generic) {

            let nodeAnswers = new Array();


            // iterate answers
            for (let j = 0; j < node.output.generic.length; j++) {


                // iterate answer variations
                let answers = node.output.generic[j].values;


                for (let i = 0; i < answers.length; i++) {
                    let text = answers[i].text;
                    let answer = '';
                    try {
                        answer =  JSON.parse(text);
                        nodeAnswers.push(answer);
                    }
                    catch(error) {
                        //
                    }
                }

            }

            answerArray.push({title: nodeTitle.toLowerCase() , answers: nodeAnswers});
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
    this.createOrCleanDir(outDir);


    // build the nlu.md
    let intents ='';

    let intentKeys = Array.from(intentsMap.keys()).sort(); // sort keys so that intents are written alphabetically sorted


    for (const intent of intentKeys) {
        let intentTitle = '## intent:' + intent + '\n';
        let exampleArray = intentsMap.get(intent).sort();
        let exampleList = yaml.stringify(exampleArray);

        intents += intentTitle + exampleList + '\n';
    }

    let entities ='';

    for (const entity of entityArray) {
        let allSynonyms =  new Array();
        let entity_name = entity.entity;
        let entity_title = '## synonym:' + entity_name;
        if (entity_name === 'pt_country_code') {
            console.debug(entity_title);
        }

        //entities += entity_title;

        for (let j = 0; j < entity.values.length; j++) {
            if (entity.values[j].synonyms !== undefined) {

                let synonymsTitle = entity.values[j].value;
                let entitySynomymsTitle = '## synonym:' + synonymsTitle + '\n';
                let synonimsList =  yaml.stringify(entity.values[j].synonyms);
                entities += entitySynomymsTitle;
                entities += synonimsList;
                entities += '\n';

                for (const synonym of entity.values[j].synonyms) {
                    allSynonyms.push({synonym: synonym,synonymsTitle: synonymsTitle,entity_name});
                }
            }
        }


        // replace entities in the intents with RASA entity annotations
        // (@([a-z|_]+):([a-z]+))

        // to replace
        if (entity_name === 'pt_geography') {
            console.debug(entity_title);
        }


        let entityToReplace = "@" + entity.entity; // e.g. @pt_geography

        while (intents.search(entityToReplace) > -1) {
            var randomSynonym = allSynonyms[Math.floor(Math.random() * allSynonyms.length)];
            let annotation = '[' + randomSynonym.synonym + ']' + '(' + entity_name + ':' + randomSynonym.synonymsTitle + ')';
            intents = intents.replace(entityToReplace, annotation);
        }


    }

    let nlu = intents + '\n\n' + entities;
    //let nlu =  entities;
    this.writeStringToFile(nlu,  outDir+ '/nlu.md');

    // domain


    let domainIntents ='intents: \n' + yaml.stringify(intentKeys,{indent:4}) + '\n';
    let groupedAnswers = groupBy(answersArray, 'title')

    let responses = {}
    for (const answer of answersArray) {
        let answers = new Array();
        for (const a of answer.answers) {
            answers.push(a);
        }

        let utterKey = 'utter_' + answer.title;
        responses[utterKey] = new Array();
        responses[utterKey].push({ custom : { answers : answers} });

    }


    let domain = {intents: intentKeys, responses: responses}
    let domainStr = yaml.stringify(domain)

    this.writeStringToFile(domainStr, outDir + '/domain.yml');

    // stories
    let stories = '';
    for (const intent of intentKeys) {
        let utterName = 'utter_' + intent;
        if (responses[utterName] !== undefined) {
            let story = '## ' + intent + '\n';
            story += '* ' + intent + '\n';
            story += '  - ' + utterName + '\n\n';
            stories += story;
        }
    }

    this.writeStringToFile(stories, outDir + '/stories.md');


}

var groupBy = function(xs, key) {
    return xs.reduce(function(rv, x) {
        (rv[x[key]] = rv[x[key]] || []).push(x);
        return rv;
    }, {});
};



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






