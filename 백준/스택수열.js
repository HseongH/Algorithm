const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const loop = input.shift();
const stack = [];
let answer = [];
let count = 1;

for (let i = 0; i < loop; i++) {
  const number = parseInt(input[i], 10);

  while (count <= number) {
    stack.push(count);
    answer.push('+');
    count++;
  }

  if (stack[stack.length - 1] !== number) {
    answer = ['NO'];
    break;
  }

  answer.push('-');
  stack.pop();
}

console.log(answer.join('\n'));
