function solution(k, m, score) {
  score.sort((a, b) => b - a);

  return Array.from({ length: Math.floor(score.length / m) }).reduce(
    (acc, _, index) => (acc += score[m - 1 + m * index] * m),
    0
  );
}

console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]));
