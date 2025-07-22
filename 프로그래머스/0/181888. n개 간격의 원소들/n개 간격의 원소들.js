function solution(num_list, n) {
    return num_list.filter((num, idex) => idex % n === 0);
}