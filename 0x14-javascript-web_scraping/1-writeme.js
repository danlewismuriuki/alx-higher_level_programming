#!/usr/bin/node
// write a string to a file

/**
 * write a string to a file
 *
 * This script takes two args from the cmd line argument
 * It writed the provided string to the specified file
 *
 * @param {string} filepath to the file to write
 * @param {string} content - the string to write the file
 * @returns {void}
 */

// import fs module
const fs = require('fs');

// get the file path from the cmd
const filepath = process.argv[2];

// check if fil path is provided
if (!filepath) {
  console.error('Usage: node 1-writeme.js <filepath>');
  process.exit(1);
}

// Get the content to write from the cmd
const content = process.argv[3];

// check if the content is provided
if (!content) {
  // display message if content is absent
  console.log('No content to print');
  process.exit(1);
}

// write contet to the specified file
fs.writeFile(filepath, content, 'utf-8', err => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content successfully written to ${filepath}`);
  }
});
