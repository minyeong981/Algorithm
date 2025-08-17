function solution(n, t, m, p) {
    let game = '';
    let answer = '';
    for (let i=0; i < t*m+1; i++) {
        game += i.toString(n)
    }
    
    for (let i=0; i < t; i++) {
        answer += game[i*m + (p-1)]
    }
    return answer.toUpperCase();
}