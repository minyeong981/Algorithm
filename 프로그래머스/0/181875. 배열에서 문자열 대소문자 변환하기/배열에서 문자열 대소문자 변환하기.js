function solution(strArr) {
    return strArr.map((str, idx) => {
        if (idx % 2) return str.toUpperCase();
        return str.toLowerCase();
    });
}