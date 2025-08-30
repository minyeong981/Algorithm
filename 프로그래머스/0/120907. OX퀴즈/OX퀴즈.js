function solution(quiz) {
    const answer = [];

    function calc(x, op, y) {
        switch(op) {
            case '+': return x+y; break;
            case '-': return x-y;
        }
    }
    
    for (const q of quiz) {
        const [x, op, y, equalSign, result] = q.split(' ');
        if (calc(Number(x), op, Number(y)) === parseInt(result)) {
            answer.push('O');
        } else {
            answer.push('X');
        }
    }
    
    
    return answer;
}