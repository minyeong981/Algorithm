function solution(a, b) {
    let ab = String(a) + String(b);
    let ba = String(b) + String(a);
    
    if (ab > ba) {
        return Number(ab)
    } else {
        return Number(ba)
    }
}