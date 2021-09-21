const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const loop = input.shift();

for (let i = 0; i < loop; i++) {
  const brackets = input[i];
  const stack = [];

  for (let j = 0; j < brackets.length; j++) {
    const bracket = brackets[j];

    if (bracket === '(') {
      stack.push(bracket);
    } else {
      if (stack.length) stack.pop();
      else {
        stack.push(bracket);
        break;
      }
    }
  }

  console.log(stack.length ? 'NO' : 'YES');
}
