function solution(myString, pat) {
    let string = '';
    [...myString].forEach(str => string += (str === 'A' ? 'B' : 'A'));
    return string.includes(pat) ? 1 : 0;
}