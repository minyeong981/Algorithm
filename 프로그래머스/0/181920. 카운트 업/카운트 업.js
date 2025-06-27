function solution(start_num, end_num) {
    let answer = [];
    for (let num = start_num; num < end_num+1; num++) {
        answer.push(num);
    }
    return answer;
}