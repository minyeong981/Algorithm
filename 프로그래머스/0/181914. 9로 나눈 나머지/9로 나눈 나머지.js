function solution(number) {
    return number.split('').map(Number).reduce((acc, cur) => acc + cur, 0) % 9;
}