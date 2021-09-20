const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const len = input.shift();

for (let i = 0; i < len; i++) {
  const word = input[i].split(' ');
  const result = word.map((part) => {
    const alpha = part.split('').reverse().join('');

    return alpha;
  });

  console.log(result.join(' '));
}
