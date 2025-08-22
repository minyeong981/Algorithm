function solution(age) {
    let answer = '';
    const alphabet = 'abcdefghijkimlopqrstuvwxyz';
    String(age).split('').forEach(num => answer += alphabet[parseInt(num)])
    return answer;
}