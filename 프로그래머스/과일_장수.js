function solution(k, m, score) {
  const count = Math.floor(score.length / m);
  const target = score.sort((a, b) => b - a).slice(0, count * m);

  return Array.from({ length: count }).reduce(
    (acc, _, index) => (acc += target[m - 1 + m * index] * m),
    0
  );
}

console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]));
