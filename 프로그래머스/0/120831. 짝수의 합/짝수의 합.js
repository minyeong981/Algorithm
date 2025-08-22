function solution(n) {
    const answer = Array.from({length: n+1}, (_, i) => i);
    return answer.filter(number => number % 2 === 0).reduce((acc, cur) => acc+cur, 0);
}