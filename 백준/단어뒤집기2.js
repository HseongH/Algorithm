const input = require('fs').readFileSync('예제.txt').toString();
const result = [];

const regExp = /<+\w>+/g;
const string = input.match(regExp);
// console.log(result.join(' '));
