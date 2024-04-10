#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let k = c;
    if (!c) {
      k = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += k;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
