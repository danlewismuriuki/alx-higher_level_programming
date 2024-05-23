#!/usr/bin/node

// import request
const request = require('request');

// Check if the Movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make HTTP GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Extract character URLs from the movie data
  const characterURLs = movieData.characters;

  // Iterate through each character URL and make a request to fetch the character data
  characterURLs.forEach(characterURL => {
    request(characterURL, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the character data
      const characterData = JSON.parse(body);

      // Print the character name
      console.log(characterData.name);
    });
  });
});
