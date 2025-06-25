function solution(n, answer = []) {
    answer.push(n);
    if (n === 1) return answer;
    if (n % 2) {
        return solution(3 * n + 1, answer);
    } else {
        return solution(n/2, answer);
    }
    return answer;
}