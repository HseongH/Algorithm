const [n, k] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .split(' ')
  .map((e) => +e);

const array = Array.from({ length: n }, (v, i) => i + 1);
const result = [];

while (array.length) {
  for (let i = 0; i < k - 1; i++) array.push(array.shift());

  result.push(array.shift());
}

console.log(`<${result.join(', ')}>`);
