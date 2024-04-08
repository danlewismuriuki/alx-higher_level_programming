#!/usr/bin/node
const argcount = process.argv;

if (argcount[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argcount[2]);
}
