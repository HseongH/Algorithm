function solution(food) {
  food.shift();

  return food.reduce((acc, cur, index) => {
    const target = acc.split('0');
    const repeat = Math.floor(cur / 2);

    return (
      (acc =
        target[0] +
        `${index + 1}`.repeat(repeat) +
        '0' +
        `${index + 1}`.repeat(repeat)) + target[1]
    );
  }, '0');
}

console.log(solution([1, 3, 4, 6]));
