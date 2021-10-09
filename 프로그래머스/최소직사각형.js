function solution(sizes) {
  const MAX_VALUE = Math.max.apply(
    null,
    sizes.map((size) => size[0] * size[1])
  );
  const areas = [];

  for (let i = 0; i < sizes.length; i++) {
    const hoz = sizes[i][0];

    for (let j = 0; j < sizes.length; j++) {
      const ver = sizes[j][1];
      const area = hoz * ver;

      if (area >= MAX_VALUE) areas.push(area);
    }
  }

  return Math.min.apply(null, areas);
}
