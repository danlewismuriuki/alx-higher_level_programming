#!/usr/bin/node

// import request module
const request = require('request');

// first argument is the url to request
const url = process.argv[2];

// Make an HTTP GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // if there are no erros print HTTP request
    console.log('code:', response.statusCode);
  }
});
