function solution(a, b) {
  return Array.from(
    { length: a > b ? a - b + 1 : b - a + 1 },
    (v, i) => (a < b ? a : b) + i
  ).reduce((acc, cur) => acc + cur);
}
