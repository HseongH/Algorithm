function solution(babbling) {
  return babbling.reduce(
    (acc, cur) =>
      (acc += cur.replace(/(aya|ye|ma|woo)(?!\1)/g, '') === '' ? 1 : 0),
    0
  );
}
