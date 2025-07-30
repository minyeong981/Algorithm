function solution(binomial) {
    let [a, op, b] = binomial.split(' ');
    a = parseInt(a);
    b = parseInt(b);
    
    switch(op) {
        case '+': return a+b;
        case '-': return a-b;
        case '*': return a*b;
    }
}