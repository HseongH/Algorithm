function solution(left, right) {
  let answer = 0;

  for (let i = left; i <= right; i++) {
    let divisorCount = i === 1 ? 1 : 2;

    if (Math.sqrt(i) % 1 === 0 && i !== 1) divisorCount += 1;

    for (let j = 2; j * j < i; j++) {
      if (i % j) divisorCount += 2;
    }

    answer += divisorCount % 2 === 0 ? i : i * -1;
  }

  return answer;
}
