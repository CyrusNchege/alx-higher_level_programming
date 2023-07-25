#!/usr/bin/node


const fs = require('fs');

function writeToFile(filePath, content) {
  fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Successfully wrote to ${filePath}`);
    }
  });
}

// Command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Usage: node 1-writeme.js <file-path> <string-to-write>');
} else {
  writeToFile(filePath, content);
}
