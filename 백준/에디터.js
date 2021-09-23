const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const initialValue = input.shift();
const loop = input.shift();

const stackLeft = initialValue.split('');
const stackRight = [];

for (let i = 0; i < loop; i++) {
  const [command, value] = input[i].split(' ');

  switch (command) {
    case 'L':
      if (stackLeft.length) stackRight.push(stackLeft.pop());
      break;

    case 'D':
      if (stackRight.length) stackLeft.push(stackRight.pop());
      break;

    case 'B':
      if (stackLeft.length) stackLeft.pop();
      break;

    default:
      stackLeft.push(value);
      break;
  }
}

console.log(stackLeft.concat(stackRight.reverse()).join(''));
