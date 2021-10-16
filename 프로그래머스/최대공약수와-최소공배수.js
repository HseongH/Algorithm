function getCommonDivisor(a, b) {
  if (b === 0) return a;

  return getCommonDivisor(b, a % b);
}

function solution(n, m) {
  const commonDivisor = getCommonDivisor(Math.max(n, m), Math.min(n, m));

  return [commonDivisor, commonDivisor * parseInt(n / commonDivisor) * parseInt(m / commonDivisor)];
}
