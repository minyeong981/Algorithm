function solution(ineq, eq, n, m) {
    let result = 0;
    switch (ineq+eq) {
        case ">=" : case ">!" :
            result = n;
            break;
        case "<=" : case "<!" :
            result = m;
            break;
    }
    if (result === Math.max(n, m)) {
        return 1
    } else {
        return 0
    }
}