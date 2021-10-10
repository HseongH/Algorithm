function solution(arr1, arr2) {
  return arr1.map((x, i) => x.map((y, j) => y + arr2[i][j]));
}
