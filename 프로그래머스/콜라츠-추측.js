function solution(num, count = 0) {
  if (num === 1) return count >= 500 ? -1 : count;

  return num % 2 ? solution(num * 3 + 1, count + 1) : solution(parseInt(num / 2), count + 1);
}
