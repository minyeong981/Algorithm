function solution(arr, queries) {
    for (const [start, end] of queries) {
        for (let i = start; i <= end; i++) {
            arr[i] += 1;
        }
    }
    return arr;
}
