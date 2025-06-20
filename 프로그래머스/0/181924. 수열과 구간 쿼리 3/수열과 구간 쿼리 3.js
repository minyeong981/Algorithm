function solution(arr, queries) {
    let temp = 0;
    for (let idx = 0; idx < queries.length; idx++) {
        temp = arr[queries[idx][0]];
        arr[queries[idx][0]] = arr[queries[idx][1]];
        arr[queries[idx][1]] = temp;
    }
    return arr;
}