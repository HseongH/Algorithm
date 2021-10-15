function solution(N, stages) {
  const percentages = [];
  let length = stages.length;

  for (let i = 1; i < N + 1; i++) {
    const count = stages.filter((stage) => stage === i).length;

    percentages.push([i, count / length]);

    length -= count;
  }

  return percentages.sort((a, b) => b[1] - a[1]).map((percentage) => percentage[0]);
}
