const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const loop = input.shift();

const deque = [];
const result = [];

for (let i = 0; i < loop; i++) {
  const [command, value] = input[i].split(' ');

  switch (command) {
    case 'push_front':
      deque.unshift(value);
      break;

    case 'push_back':
      deque.push(value);
      break;

    case 'pop_front':
      result.push(deque.length ? deque.shift() : -1);
      break;

    case 'pop_back':
      result.push(deque.length ? deque.pop() : -1);
      break;

    case 'size':
      result.push(deque.length);
      break;

    case 'empty':
      result.push(Number(deque.length === 0));
      break;

    case 'front':
      result.push(deque[0] || -1);
      break;

    default:
      result.push(deque[deque.length - 1] || -1);
  }
}

console.log(result.join('\n'));
