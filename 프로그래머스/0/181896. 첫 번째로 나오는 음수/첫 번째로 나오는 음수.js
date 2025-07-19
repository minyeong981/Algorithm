function solution(num_list) {
    for (const ele of num_list) {
        if (ele < 0) return num_list.indexOf(ele);
    }
    return -1;
}