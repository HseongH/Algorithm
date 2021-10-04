function solution(enter, leave) {
  const temp = {};

  while (leave.length) {
    const ePerson = enter.shift();
    const lPerson = leave.shift();

    temp[lPerson] ? (temp[lPerson].isAppend = false) : leave.unshift(lPerson);

    for (const [key, value] of Object.entries(temp)) {
      if (value.isAppend) temp[key].count += 1;
    }

    if (ePerson) temp[ePerson] = { count: 0, isAppend: true };
  }

  return Object.values(temp).map(({ count }) => count);
}
