function solution(arr) {
    if (arr.length === 1 || arr === [10]) {
        return [-1]
    } else {
        let minV = Math.min(...arr);
        arr.splice(arr.indexOf(minV), 1)
        return arr
    }
    
}