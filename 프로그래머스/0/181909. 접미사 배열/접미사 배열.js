function solution(my_string) {
    const result = [];
    const reversedString = my_string.split('');
    for (let i = my_string.length - 1; i >= 0; i--) {
        result.push(reversedString.slice(i).join(''))
    }
    return result.sort();
}