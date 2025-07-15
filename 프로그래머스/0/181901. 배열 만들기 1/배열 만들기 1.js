function solution(n, k) {
    const answer = [];
    let number = 1;
    let i = 1;
    while (i*k <= n) {
        answer.push(i*k);
        i++
    }
    return answer;
}