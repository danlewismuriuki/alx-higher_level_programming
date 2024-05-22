#!/usr/bin/node

// Import the fs module to work with the file system
const fs = require('fs');

// get the file path fromm the cmd line
const filepath = process.argv[2];

// check if a file path is provided
if (!filepath) {
  // print Usage insructions if no file path is provided
  console.error('Usage: node 0-readme.js <filepath>');
  // Exit the script with non-zero status code indicates failure
  process.exit(1);
}

// read the content of the file asynchronously
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    // If an errro occured during printing print teh error
    console.error(err);
  } else {
    // print the content of the file
    console.log(data);
  }
});
