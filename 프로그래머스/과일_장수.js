function solution(k, m, score) {
  score.sort();

  return Array.from(
    { length: Math.floor(score.length / m) },
    (_, i) => i
  ).reduce((acc, cur) => (acc += score[score.length - m * (cur + 1)] * m), 0);
}

console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]));
