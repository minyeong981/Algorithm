function solution(numbers) {
    let n = numbers.length;
    const total = numbers.reduce((acc, cur) => acc+cur, 0);
    return total/n;
}