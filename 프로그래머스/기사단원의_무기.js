function solution(number, limit, power) {
  let answer = 1;
  const numbers = Array.from({ length: number - 1 }, (_, i) => i + 2);

  for (let i = 0; i < numbers.length; i++) {
    let dividorCount = Math.sqrt(numbers[i]) % 1 === 0 ? 3 : 2;

    for (let j = 2; j < Math.sqrt(numbers[i]); j++) {
      if (numbers[i] % j !== 0) {
        continue;
      }

      dividorCount += 2;
    }

    answer += dividorCount > limit ? power : dividorCount;
  }

  return answer;
}
