function solution(arr) {
    return arr.reduce((x, num) => [...x, ...new Array(num).fill(num)], []);
}