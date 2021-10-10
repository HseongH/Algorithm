function solution(x) {
  let temp = x;
  let divisor = 0;

  while (temp) {
    divisor += temp % 10;
    temp = Math.floor(temp / 10);
  }

  return !(x % divisor);
}
