function solution(table, languages, preference) {
  const answer = table.sort().reduce((acc, cur) => {
    const columns = cur.split(' ');

    return {
      ...acc,
      [columns[0]]: languages.reduce((acc, language, i) => {
        const column = columns.slice(1);
        const rank = column.indexOf(language);
        const score = rank !== -1 ? (column.length - rank) * preference[i] : 0;

        return acc + score;
      }, 0),
    };
  }, {});

  return Object.keys(answer)[
    Object.values(answer).reduce((acc, cur, i, arr) => (arr[acc] < cur ? i : acc), 0)
  ];
}
