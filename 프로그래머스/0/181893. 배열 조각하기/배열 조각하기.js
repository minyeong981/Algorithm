function solution(arr, query) {
    let answer = arr;
    for (const index in query) {
        if (index % 2) {
            answer = answer.slice(query[index]);
        } else {
            answer = answer.slice(0, query[index]+1);
        } 
    }
    return answer;
}