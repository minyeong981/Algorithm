function solution(arr, queries) {
    return queries.map(([s, e, k]) => {
        let sliced = arr.slice(s, e + 1)
            .filter(v => v > k)
            .sort((a, b) => a - b);  // 숫자 오름차순 정렬

        return sliced.length > 0 ? sliced[0] : -1;
    });
}
