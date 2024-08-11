#!/usr/bin/node
/**
 * The script fetches characters from the star wars movies
 * given the id of the film
 */

const request = require('request');

function makeGetRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }

      if (response.statusCode !== 200) {
        console.error(`Error ${response.statusCode}`);
      }
      const jsonData = JSON.parse(body);
      resolve(jsonData);
    });
  });
}

async function fecthNameofCharacter (character) {
  try {
    const data = await makeGetRequest(character);
    return data.name;
  } catch (error) {
    console.error('Error fetching name');
  }
}

async function fetchCharacters (characters) {
  const chrs = [];

  for (const character of characters) {
    const name = await fecthNameofCharacter(character);
    chrs.push(name);
  }

  chrs.forEach((chr) => {
    console.log(chr);
  });
}

async function fetchMovie (id) {
  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
    const data = await makeGetRequest(url);
    const characters = data.characters;
    // console.log(data['characters']);
    fetchCharacters(characters);
  } catch (error) {
    console.error('Error Fetching data', error);
  }
}

function main () {
  const args = process.argv;

  if (args.length !== 3) {
    console.log('Usage: ./0-starwars_characters.js <id>');
    return;
  }

  const id = args[2];
  fetchMovie(id);
}

main();
