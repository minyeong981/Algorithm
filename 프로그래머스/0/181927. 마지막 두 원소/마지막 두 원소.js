function solution(num_list) {
    let n = num_list.length-1;
    let answer = num_list;
    (answer[n] > answer[n-1]) ? answer.push(answer[n] - answer[n-1]) : answer.push(answer[n]*2);
    return answer;
}