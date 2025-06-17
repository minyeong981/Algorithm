function solution(num_list, n) {
    if (n === num_list.length) {
        return num_list
    };
    
    for (let i = 0; i < num_list.length; i++) {
        if (i < n) {
            num_list.push(num_list.shift());
        } else {
            return num_list
        }
    }
}