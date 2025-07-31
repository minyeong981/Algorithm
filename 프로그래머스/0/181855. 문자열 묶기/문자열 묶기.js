function solution(strArr) {
    let answer = new Map();
    strArr.forEach(str => {
        answer.set(str.length, (answer.get(str.length) || 0) + 1);
    })

    return Math.max(...answer.values());
}