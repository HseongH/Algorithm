const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

const alphabet = [
  'a',
  'b',
  'c',
  'd',
  'e',
  'f',
  'g',
  'h',
  'i',
  'j',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'w',
  'x',
  'y',
  'z',
];
const answer = [];

alphabet.forEach((alpha) => {
  const index = input.indexOf(alpha);

  answer.push(index);
});

console.log(answer.join(' '));
