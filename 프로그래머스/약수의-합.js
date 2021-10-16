function solution(n) {
  const arr = new Set();
  let answer = 0;

  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      arr.add(i);
      arr.add(parseInt(n / i));
    }
  }

  for (const item of arr) {
    answer += item;
  }

  return answer;
}
