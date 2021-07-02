function recur(operator, arr, n) {
  if (arr.length === n) {
    const temp = arr.slice();
    operator.push(temp);
    return;
  }

  arr.push('+');
  recur(operator, arr, n);
  arr.pop();

  arr.push('-');
  recur(operator, arr, n);
  arr.pop();
}

function solution(numbers, target) {
  let answer = 0;
  const operator = [];

  recur(operator, [], numbers.length);

  for (let i = 0; i < operator.length; i++) {
    let calculation = '';

    for (let j = 0; j < operator[i].length; j++) {
      calculation += operator[i][j] + numbers[j];
    }

    if (eval(calculation) === target) answer++;
  }

  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
