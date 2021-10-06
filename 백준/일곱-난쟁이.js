let input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .split('\n')
  .map((e) => +e.trim());
const overflow = input.reduce((acc, cur) => acc + cur) - 100;

for (let i = 0; i < 8; i++) {
  if (input[i] > overflow) continue;

  for (let j = i + 1; j < 9; j++) {
    if (input[i] + input[j] === overflow) {
      input = input.filter((e) => e !== input[i] && e !== input[j]).sort((a, b) => a - b);
      break;
    }
  }

  if (input.length === 7) break;
}

console.log(input.join('\n'));
