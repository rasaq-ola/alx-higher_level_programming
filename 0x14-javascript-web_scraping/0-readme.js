#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err.message);
    process.exit(1);
  } else {
    console.log(data);
  }
});
