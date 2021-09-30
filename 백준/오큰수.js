const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const length = +input[0];
const list = input[1].split(' ').map((e) => +e);

const stack = [];
const result = Array.from({ length: length }, () => -1);

for (let i = 0; i < length; i++) {
  while (stack.length && list[stack[stack.length - 1]] < list[i]) {
    result[stack.pop()] = list[i];
  }

  stack.push(i);
}

console.log(result.join(' '));
