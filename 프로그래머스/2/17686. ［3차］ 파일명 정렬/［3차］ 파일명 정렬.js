function solution(files) {
  const regex = /^([a-zA-Z .-]+)(\d{1,5})(.*)$/;

  return files
    .map(file => {
      const [, head, number, tail] = file.match(regex);
      return {
        original: file,
        head: head.toLowerCase(),
        number: parseInt(number),
      };
    })
    .sort((a, b) => {
      if (a.head < b.head) return -1;
      if (a.head > b.head) return 1;
      if (a.number !== b.number) return a.number - b.number;
      return 0;
    })
    .map(obj => obj.original);
}
