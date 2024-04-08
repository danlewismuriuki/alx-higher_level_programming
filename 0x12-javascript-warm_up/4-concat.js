#!/usr/bin/node

const argcount = process.argv.length;
const word = 'is';

if (argcount >= 4) {
  console.log(`${process.argv[2]} ${word} ${process.argv[3]}`);
} else if (argcount >= 3) {
  console.log(`${process.argv[2]} ${word} undefined`);
} else {
  console.log(`undefined ${word} undefined`);
}
