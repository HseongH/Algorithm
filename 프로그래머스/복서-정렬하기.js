function solution(weights, head2head) {
  return head2head
    .reduce((acc, cur, i) => {
      const win = /W/gi;
      const none = /N/gi;
      const winCounter = cur.match(win);
      const noneCounter = cur.match(none);
      const score = winCounter ? winCounter.length / (cur.length - noneCounter.length) : 0;
      const weightTotal = weights.filter(
        (weight, j) => weights[i] < weight && cur[j] === 'W'
      ).length;

      return [...acc, { index: i + 1, score, weightTotal }];
    }, [])
    .sort((a, b) => {
      return (
        b.score - a.score ||
        b.weightTotal - a.weightTotal ||
        weights[b.index - 1] - weights[a.index - 1] ||
        a.index - b.index
      );
    })
    .map(({ index }) => index);
}
