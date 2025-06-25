function solution(n) {
    let answer = [];
    while (n > 0) {
        answer.push(n);
        if (n === 1) break;
        (n % 2) ? (n = 3 * n + 1) : (n /= 2);
    } 
    return answer;
}