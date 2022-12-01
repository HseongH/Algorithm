function solution(k, score) {
  const stack = [];
  const answer = [];

  score.forEach((item) => {
    stack.push(item);
    stack.sort((a, b) => a - b);

    if (stack.length > k) stack.shift();

    answer.push(stack[0]);
  });

  return answer;
}

function solution(k, score) {
  const stack = [];

  return score.reduce((acc, cur) => {
    stack.push(cur);
    stack.sort((a, b) => a - b);

    if (stack.length > k) stack.shift();

    return acc.concat(stack[0]);
  }, []);
}

function solution(k, score) {
  const stack = [];

  return score.reduce((acc, cur) => {
    stack.push(cur);
    stack.sort((a, b) => a - b);

    if (stack.length <= k) return acc.concat(stack[0]);

    return acc.concat(stack[stack.length - k]);
  }, []);
}

function solution(k, score) {
  const stack = [];
  const answer = [];

  score.forEach((item) => {
    stack.push(item);
    stack.sort((a, b) => a - b);

    if (stack.length <= k) {
      answer.push(stack[0]);

      return;
    }

    answer.push(stack[stack.length - k]);
  });

  return answer;
}
