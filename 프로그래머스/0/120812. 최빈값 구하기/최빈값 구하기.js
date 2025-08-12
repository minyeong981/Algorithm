function solution(array) {
    const count = new Map();
    array.forEach((value) => {
        count.set(value, (count.get(value) || 0)+1);
    })
    let answer = -1;
    let maxV = -1;
    for(const [key, value] of count.entries()) {
        if (maxV <= value) {
            answer = key;
            if (maxV === value) {
                answer = -1;
            }
            maxV = value;
        }
    }
    return answer;
}