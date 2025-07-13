function solution(intStrs, k, s, l) {
    return intStrs.map(number => parseInt(number.substr(s, l))).filter(value => value > k);
}