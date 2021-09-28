const input = require('fs').readFileSync('예제.txt').toString();
const result = [];

let convert = true;
let target = [];

for (let i = 0; i < input.length; i++) {
  const word = input[i];

  if (word === '<') {
    if (target.length) {
      result.push(target.join(''));
      target.splice(0, target.length);
    }

    convert = false;
  } else if (word === '>' || (word === ' ' && convert)) {
    target.push(word);
    result.push(target.join(''));
    target.splice(0, target.length);

    continue;
  }

  convert ? target.unshift(word) : target.push(word);
  console.log(target);
}

if (target.length) {
  result.push(target.join(''));
}

console.log(result.join(''));
