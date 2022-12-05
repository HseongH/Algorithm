function solution(s) {
  let answer = 0;
  let stack1 = [s[0]];
  let stack2 = [];

  for (let i = 1; i < s.length; i++) {
    if (s[i] === stack1[stack1.length - 1]) {
      stack1.push(s[i]);
    } else {
      stack2.push(s[i]);
    }

    if (stack1.length === stack2.length) {
      stack1 = [];
      stack2 = [];
      answer++;

      i++;
      s[i] && stack1.push(s[i]);
    }
  }

  return stack1.length !== 0 || stack2.length !== 0 ? answer + 1 : answer;
}
