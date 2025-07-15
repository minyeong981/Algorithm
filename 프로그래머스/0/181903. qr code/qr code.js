function solution(q, r, code) {
    let answer = '';
    for (const index in code) {
        if (index % q === r)  {
          answer += code[index]  
        }
    }
    return answer;
}