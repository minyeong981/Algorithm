function solution(arr, k) {
    const answer = [];
    for (let number of arr) {
        if (answer.length === k) return answer;
        if (!answer.includes(number)) {
            answer.push(number);
        }
    }
    
    const len = answer.length;
    if (len !== k) {
        for (let i=0; i < k-len; i++) {
            answer.push(-1);
        }        
    }
    return answer;
}