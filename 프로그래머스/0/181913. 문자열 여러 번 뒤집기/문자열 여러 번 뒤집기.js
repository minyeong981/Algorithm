function solution(my_string, queries) {
    let answer = my_string;
    for (let [s, e] of queries) {
        let reversedString = answer.slice(s, e+1).split('').reverse().join('');
        answer = answer.slice(0, s) + reversedString + answer.slice(e+1);
    }
    return answer;
}