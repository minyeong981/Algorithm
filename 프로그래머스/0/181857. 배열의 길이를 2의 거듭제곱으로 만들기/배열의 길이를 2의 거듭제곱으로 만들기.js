function solution(arr) {
    let arrLength = arr.length;
    let i = 0;
    while (Math.pow(2, i) < arrLength) i++;
    let targetLength = Math.pow(2, i);
    while (arr.length < targetLength) arr.push(0);
    return arr;
}
