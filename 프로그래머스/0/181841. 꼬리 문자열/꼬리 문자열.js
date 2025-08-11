function solution(str_list, ex) {
    return str_list.map(value => {return (value.includes(ex) ? '' : value)}).reduce((acc, cur) => acc+cur, '');
}