function solution(n, k) {
    const numbers = n.toString(k).split('0');
    let answer = numbers.map(n => {
        let num = Number(n);
        let endNum = parseInt(Math.sqrt(num), 10);
        if (num === 1) return;
        for (let i=2; i <= endNum; i++) {
            if (num % i === 0) return;
        }
        return n;
    })

    return answer.filter(Boolean).length;
}