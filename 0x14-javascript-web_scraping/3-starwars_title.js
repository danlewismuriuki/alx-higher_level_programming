#!/usr/bin/node

// import the request module
const request = require('request');

// get the movie argument from the cmd
const movieID = process.argv[2];

// api url with an appended movieid
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make an HTTP GET request to the Star Wars API endpoint
request(url, (error, response, body) => {
  if (error) {
    // If there's an error, log the error message
    console.error(error);
  } else {
    // If the request is successful, parse the JSON response body
    const contentdata = JSON.parse(body);
    // Extract and log the title of the movie from the parsed data
    console.log(contentdata.title);
  }
});
