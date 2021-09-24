const [n, k] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .split(' ')
  .map((e) => +e);

const array = Array.from({ length: n }, (v, i) => i + 1);
const result = [];
let ptr = 0;

while (array.length) {
  ptr = (ptr + (k - 1)) % array.length;

  result.push(array.splice(ptr, 1));
}

console.log(`<${result.join(', ')}>`);
