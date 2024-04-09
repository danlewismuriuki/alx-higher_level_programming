#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    // Recursive case: n * factorial(n - 1)
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
