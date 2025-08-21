function solution(my_string, n) {
    let answer = '';
    for (const alpha of my_string) {
        answer += alpha.repeat(n)
    }
    return answer;
}