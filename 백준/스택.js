const array = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const stack = [];
const result = [];

const loop = array.shift();

for (let i = 0; i < loop; i++) {
  const [key, value] = array[i].split(' ');
  const length = stack.length;

  switch (key) {
    case 'pop':
      result.push(length ? stack.pop() : -1);
      break;

    case 'size':
      result.push(length);
      break;

    case 'empty':
      result.push(Number(length === 0));
      break;

    case 'top':
      result.push(length ? stack[length - 1] : -1);
      break;

    default:
      stack.push(value);
  }
}

console.log(result.join('\n'));
