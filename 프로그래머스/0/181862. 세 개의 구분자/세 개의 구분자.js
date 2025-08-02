function solution(myStr) {
    const answer = [];
    const reg = /^[a-c]$/;
    let word = '';
    for (let i in myStr) {
        if (!reg.test(myStr[i])) {
            word += myStr[i];
        } else {
            if (word.length) answer.push(word);
            word = ''
        } 
    }
    if (word.length) answer.push(word); 
    return answer.length === 0 ? ["EMPTY"] : answer;
}