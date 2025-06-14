function solution(arr) {
    if (arr.length === 1 || arr === [10]) {
        return [-1]
    } else {
        let minV = Math.min(...arr);
        let result = arr.filter(ele => ele !== minV)
        return result
    }
    
}