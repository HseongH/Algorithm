function solution(s, n) {
  let answer = '';

  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') {
      answer += s[i];
      continue;
    }

    const convert = s[i].toUpperCase().charCodeAt() + n;
    const standard = 'Z'.charCodeAt();
    const result = convert <= standard ? convert : convert - standard + ('A'.charCodeAt() - 1);

    answer +=
      s[i] === s[i].toUpperCase()
        ? String.fromCharCode(result)
        : String.fromCharCode(result).toLowerCase();
  }

  return answer;
}

console.log(solution('z', 1));
