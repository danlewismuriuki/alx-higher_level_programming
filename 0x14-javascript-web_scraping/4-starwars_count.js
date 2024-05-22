#!/usr/bin/node

// This script takes a URL as a command-line argument
const request = require('request');

// Check if the user has provided a URL as a command-line argument
if (process.argv.length > 2) {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Filter the results to find items with a character ID containing '18'
      const result = JSON.parse(body).results.filter(item =>
        item.characters.find(id => id.match(/18/)));
      // Log the length of the filtered results
      console.log(result.length);
    }
  });
}
