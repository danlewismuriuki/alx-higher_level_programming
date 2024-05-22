#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if exactly 3 additional arguments are provided
// node, script, URL, file path)
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Extract URL and file path from command-line arguments
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
