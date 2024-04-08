#!/usr/bin/node

const argCount = process.argv.length;

if (argCount === 2) {
  console.log("No arguments passed");
} else if (argCount === 3) {
  console.log("Argument found");
} else {
  const number = +process.argv[3];

  if (isNaN(number)) {
    console.log("Not a number");
  } else {
    console.log(`My number: ${number}`);
  }
}

