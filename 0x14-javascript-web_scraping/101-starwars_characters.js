#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  const charactersPromises = charactersUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(`Invalid response: ${response.statusCode}`);
          return;
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(charactersPromises)
    .then(characters => {
      characters.forEach(character => {
        console.log(character);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
