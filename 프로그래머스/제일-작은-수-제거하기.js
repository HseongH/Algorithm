function solution(arr) {
  const min = Math.min.apply(null, arr);
  const answer = arr.filter((e) => e !== min);

  return answer.length ? answer : [-1];
}
