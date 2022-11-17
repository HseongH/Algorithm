function solution(a, b) {
  const week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
  const startDay = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];

  return week[(b - 1 + startDay[a - 1]) % 7];
}
