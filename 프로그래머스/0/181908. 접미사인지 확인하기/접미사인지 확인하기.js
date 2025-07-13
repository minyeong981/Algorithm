function solution(my_string, is_suffix) {
    const answer = 0;
    const suffix_array = my_string.split('').map((_, i) => my_string.slice(i));
    
    return suffix_array.includes(is_suffix) ? 1 : 0;
}