function solution(n) {
  let answer = '';
  const numbers = [4, 1, 2];

  while (n) {
    const index = n % 3;

    n = Math.floor(n / 3);

    if (!index) n--;

    answer = numbers[index] + answer;
  }

  return answer;
}

console.log(solution(5555555));
