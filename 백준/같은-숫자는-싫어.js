function solution(arr) {
  return arr.filter((e, i) => arr[i + 1] !== e);
}
