function solution(arr, n) {
    if (arr.length % 2) {
        return arr.map((num, idx) => {
            if (idx % 2 === 0) return num+n;
            else return num;
        })
    } else {
        return arr.map((num, idx) => {
            if (idx % 2) return num+n;
            else return num;
        })        
    }
}