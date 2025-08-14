function solution(array) {
    let answer = 0;
    for (const number of array.join('')) {
        if (number === '7') answer++;
    }
    return answer;
}