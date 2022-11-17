function solution(number) {
  let answer = 0;

  for (let i = 0; i < number.length - 2; i++) {
    for (let j = i + 1; j < number.length; j++) {
      for (let k = j + 1; k < number.length; k++) {
        answer += number[i] + number[j] + number[k] === 0 ? 1 : 0;
      }
    }
  }

  return answer;
}

console.log(solution([-2, 3, 0, 2, -5]));
