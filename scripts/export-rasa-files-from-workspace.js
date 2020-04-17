'use strict';
/*
 This script reads a watson conversation workspace in JSON format and outputs a set of files
 in the following directory structure:

 directory/
    intents/  (all intents in separate CSV files)
    entities/ (all entities in separate CSV files)
    nodes/  (all nodes, each folder in a separate file)
    answers/ (all answers)

 it takes a 2 parameters:
 - workspace file (JSON)
 - output directory
 */

let program = require('commander');
let rasaUtils = require('./rasa-utils');
let watsonUtils = require('./watson-conversation-utils');



let inputJSON ;
let outputDirectory ;

program
    .version('0.1.0')
    .usage('<inputJSONFile> <outputDirectoryPath> ')
    .arguments('<inputJSONFile> <outputDirectoryPath> ')
    .action(function (inputJSONFile, outputDirectoryPath) {
        inputJSON = inputJSONFile;
        outputDirectory = outputDirectoryPath;
    })
    .parse(process.argv);

if (typeof inputJSON === 'undefined') {
    console.error('<inputJSONFile> not  given!');
    console.info('Usage: ' + program.usage());
    process.exit(1);
}

if (typeof outputDirectory === 'undefined') {
    console.error('<outputDirectoryPath> not  given!');
    process.exit(1);
}


let sourceJSON = require(inputJSON);
let answersAttachmentsJSON = rasaUtils.extractAnswersFromJSON(sourceJSON);
let metadata = rasaUtils.extractMetadataFromJSON(sourceJSON);
let intentsMap = rasaUtils.extractIntentsFromJSON(sourceJSON);
let entityMap = watsonUtils.extractEntitiesFromJSON(sourceJSON);
let entityArray = watsonUtils.extractEntitiesFromJSONToObjectArray(sourceJSON);
let nodeArray = watsonUtils.extractNodesFromJSON(sourceJSON);

rasaUtils.writeIntentsEntitiesAnswersToFiles(metadata,intentsMap,entityArray,answersAttachmentsJSON.answers,nodeArray,outputDirectory);
