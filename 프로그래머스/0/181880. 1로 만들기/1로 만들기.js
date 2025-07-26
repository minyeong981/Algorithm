function solution(num_list) {
    let count = 0;
    num_list.forEach(num => count += calc(num));
    
    function calc(num) {
        if (num === 1) return 0
        if (num % 2) {
            return 1 + calc((num-1)/2)
        } else {
            return 1 + calc(num/2)
        }
    }
    return count;
}