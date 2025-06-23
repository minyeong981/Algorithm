function solution(n) {
    let pizza = 1;
    while (pizza*7 < n) {
        pizza++;
    }
    return pizza;
}