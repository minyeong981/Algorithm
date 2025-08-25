function solution(emergency) {
  const sorted = [...emergency].sort((a, b) => b - a);
  return emergency.map(num => sorted.findIndex(x => x === num) + 1);
}
