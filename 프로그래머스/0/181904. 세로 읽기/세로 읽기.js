function solution(my_string, m, c) {
    let answer = '';
    for (let i = 0; i < my_string.length; i += m) {
        let substr = my_string.substr(i, m);
        answer += substr[c-1];
    }
    return answer;
}