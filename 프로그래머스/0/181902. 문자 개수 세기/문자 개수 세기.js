function solution(my_string) {
    const answer = Array.from({length: 52}, _ => 0);
    for (let char of my_string) {
        const lowerIndex = char.charCodeAt() % 97
        const upperIndex = char.charCodeAt() % 64
        if (char === char.toLowerCase()) answer[lowerIndex + 26]++;
        else answer[upperIndex-1]++;
    }
    return answer;
}