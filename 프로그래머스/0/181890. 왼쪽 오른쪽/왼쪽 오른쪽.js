function solution(str_list) {
    for (const [index, char] of str_list.entries()) {
        if (char === 'l') return str_list.slice(0, index);
        else if (char === 'r') return str_list.slice(index+1);
    }
    return [];
}