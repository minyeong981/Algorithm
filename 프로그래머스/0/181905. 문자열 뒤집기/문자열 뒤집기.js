function solution(my_string, s, e) {
    var reversed_string = my_string.slice(s, e+1).split('').reverse().join('');
    return my_string.slice(0, s) + reversed_string + my_string.slice(e+1)
}