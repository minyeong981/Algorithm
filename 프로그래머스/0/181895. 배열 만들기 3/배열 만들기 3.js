function solution(arr, intervals) {
    const answer = [];
    for (const interval of intervals) {
        answer.push(...arr.slice(interval[0], interval[1]+1));
    }
    return answer;
}