#!/usr/bin/node

const { list } = require('./100-data');

const newList = list.map(function (value, index) {
  return value * index;
});

console.log(list);
console.log(newList);
