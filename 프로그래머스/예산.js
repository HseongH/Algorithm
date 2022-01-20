function solution(d, budget, isFirst) {
  if (!isFirst) d.sort();
  const sum = d.reduce((acc, cur) => acc + cur, 0);

  if (sum <= budget) return d.length;

  const maxValue = Math.max.apply(null, d);

  if (maxValue >= budget) return d.length - 1;

  d.pop();
  return solution(d, budget, true);
}

console.log(solution([1, 3, 2, 5, 4], 9));
