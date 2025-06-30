function solution(x1, x2, x3, x4) {
    let answer = false;
    if (x1 === x2 && x3 === x4 && x1 === x3 && x1) return !answer;
    else if (x1 !== x2 && x3 !== x4) return !answer;
    else if ((x1 !== x2 && x3 === x4 && x3) || (x1 === x2 && x3 !== x4 && x1)) return !answer;
    return answer;
}