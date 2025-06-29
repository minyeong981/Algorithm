function solution(l, r) {
    const answer = [];
    const queue = ['5'];
    
    while (queue.length > 0) {
        let num = queue.shift();
        let currentNum = parseInt(num);
        
        if (currentNum > r) break;
        if (currentNum >= l) answer.push(currentNum);
        
        queue.push(num + '0');
        queue.push(num + '5');
    }
    return answer.length === 0 ? [-1] : answer;
}