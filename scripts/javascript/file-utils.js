var zipdir = require('zip-dir');
var fs = require('fs');


let file_utils = {};

file_utils.zipDirectory = function (inputDir,outputZIP) {
    zipdir(inputDir ,{ saveTo: outputZIP }, function (err, buffer) {
        // `buffer` is the buffer of the zipped file
        // And the buffer was saved to `~/myzip.zip`
    });
};


file_utils.getFilesFromDir = function(fileDir){
    return fs.readdirSync(fileDir);
};


module.exports = file_utils;