function solution(num_str) {
    var array = num_str.split('').map(Number);
    return array.reduce((acc, curr) => acc+curr, 0);
}