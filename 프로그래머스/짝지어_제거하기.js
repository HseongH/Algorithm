function solution(s) {
  const stack = [];

  if (s % 2) return 0;

  for (let i = 0; i < s.length; i++) {
    const lastChild = stack.length - 1;

    lastChild < 0 || stack[lastChild] !== s[i] ? stack.push(s[i]) : stack.pop();
  }

  return !stack.length * 1;
}
