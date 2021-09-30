const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const length = input.shift();
const list = input
  .shift()
  .split(' ')
  .map((e) => +e);

const result = [];

while (list.length) {
  const target = list.shift();
  const answer = list.find((e) => e > target);

  result.push(answer || -1);
}

console.log(result.join(' '));
