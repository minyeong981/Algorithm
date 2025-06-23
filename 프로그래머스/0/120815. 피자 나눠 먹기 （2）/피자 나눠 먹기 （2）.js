function solution(n) {
    let pizza = 1;
    let piece = 6;
    while (piece % n != 0) {
        pizza += 1;    
        piece = 6 * pizza;
    }
    return pizza;      
}