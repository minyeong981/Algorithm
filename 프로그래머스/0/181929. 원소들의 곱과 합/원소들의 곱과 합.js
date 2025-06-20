function solution(num_list) {
    let x = 1;
    let sum = 0;
    for (let i=0; i < num_list.length; i++) {
        x *= num_list[i];
        sum += num_list[i];
    }
    return x < Math.pow(sum, 2) ? 1 : 0;
}