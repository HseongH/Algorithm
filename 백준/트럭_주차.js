const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const price = input
  .shift()
  .split(' ')
  .map((x) => +x);
const timeObj = input.reduce((acc, cur) => {
  const time = cur.split(' ');

  Array.from(
    { length: parseInt(time[1]) - parseInt(time[0]) },
    (_, i) => i + parseInt(time[0])
  ).forEach((x) => {
    if (acc[x]) {
      return (acc[x] += 1);
    }

    acc[x] = 1;
  });

  return acc;
}, {});

const result = Object.keys(timeObj).reduce((acc, cur) => {
  return (acc += price[timeObj[cur] - 1] * timeObj[cur]);
}, 0);

console.log(result);
