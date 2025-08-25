function solution(hp) {
    let answer = Math.trunc(hp/5);
    if (hp % 5) {
        hp %= 5;
        if (hp % 3) {
            answer += Math.trunc(hp/3);
            hp %= 3;
            answer += hp;
        } else {
            answer++;
        }
        
    }
    return Math.trunc(answer);
}