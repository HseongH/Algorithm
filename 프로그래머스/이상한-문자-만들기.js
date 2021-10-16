function solution(s) {
  return s
    .split(' ')
    .map((word) =>
      word
        .split('')
        .map((alphabet, i) =>
          alphabet.replace(alphabet, i % 2 ? alphabet.toLowerCase() : alphabet.toUpperCase())
        )
        .join('')
    )
    .join(' ');
}
