function solution(num_list) {
    const odd = num_list.filter((num, idx) => idx % 2 === 0);
    const even = num_list.filter((num, idx) => idx % 2);
    
    function sum(lst) {
        return lst.reduce((acc, curr) => acc+curr, 0);
    }

    return Math.max(sum(odd), sum(even));
}