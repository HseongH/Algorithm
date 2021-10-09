function solution(n) {
  const arr = [0, 1, 1];

  for (let i = 3; i <= n; i++) {
    arr[i] = (arr[i - 1] % 1234567) + (arr[i - 2] % 1234567);
  }

  return arr[n] % 1234567;
}
