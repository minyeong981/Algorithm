function solution(dartResult) {
    const queue = [];
    let number = '';
    for (const score of dartResult) {
        if (/^[0-9]{1}$/.test(score)) {
            number += score.toString();
            continue;
        }
        switch (score) {
            case 'S' : queue.push(Math.pow(parseInt(number), 1)); break;
            case 'D' : queue.push(Math.pow(parseInt(number), 2)); break;
            case 'T' : queue.push(Math.pow(parseInt(number), 3)); break;
            case '*' : queue[queue.length-1] *= 2; if (queue.length > 1) queue[queue.length-2] *= 2; break;
            case '#' : queue[queue.length-1] *= -1; break;
        }
        number = '';
    }
    return queue.reduce((acc, cur) => acc + cur, 0);
}