function solution(numLog) {
    let answer = '';
    let value = numLog[0];
    for (let num of numLog.slice(1)) {
        switch (num - value) {
            case 1 :
                answer += 'w';
                break;
            case -1 :
                answer += 's';
                break;
            case 10 :
                answer += 'd';
                break;
            case -10 :
                answer += 'a';
                break;
        }
        value = num;
    }
    return answer;
}