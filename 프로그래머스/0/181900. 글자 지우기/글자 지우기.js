function solution(my_string, indices) {
    let answer = my_string.split('');
    return answer.filter((ele, i) => !indices.includes(i)).join('')
}