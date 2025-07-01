function solution(n, arr1, arr2) {
    const answer = [];
    for (let i = 0; i < n; i++) {
        let binary = (arr1[i] | arr2[i]).toString(2);
        binary = binary.padStart(n, '0');
        
        let secret = '';
        for (let ele of binary) {
            ele === '1' ? secret += '#' : secret += ' ';
        }
        answer.push(secret)
    }
    return answer;
}