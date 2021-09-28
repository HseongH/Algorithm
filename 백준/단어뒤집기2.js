const input = require('fs').readFileSync('/dev/stdin').toString().trim();
const reg = /(<.+?>|\s)/g;
const temp = input.split(reg);

const result = temp.map((word) => {
  return reg.test(word) ? word : word.split('').reverse().join('');
});

console.log(result.join(''));
