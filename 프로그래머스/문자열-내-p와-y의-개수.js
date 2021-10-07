function solution(s) {
  const pMatch = s.match(/p/gi) || [];
  const yMatch = s.match(/y/gi) || [];

  return pMatch.length === yMatch.length;
}
