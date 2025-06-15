function solution(my_string, overwrite_string, s) {
    let replaced_string = my_string.substr(s, overwrite_string.length);
    let answer = my_string.substr(s).replace(replaced_string, overwrite_string);
    
    return my_string.substr(0, s) + answer
}