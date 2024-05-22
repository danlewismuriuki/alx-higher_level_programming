#!/usr/bin/node

// a script that writes a string to a file.

const fs = require('fs');

const filepath = process.argv[2];

if (!filepath) {
  console.error('Usage: node 1-writeme.js <filepath>');
  process.exit(1);
}

const content = process.argv[3];

if (!content) {
  console.log('No content to print');
  process.exit(1);
}

fs.writeFile(filepath, content, err => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content successfully written to ${filepath}`);
  }
});
