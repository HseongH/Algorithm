function solution(n) {
  const squareRoot = Math.sqrt(n);

  return squareRoot % 1 ? -1 : (squareRoot + 1) * (squareRoot + 1);
}
