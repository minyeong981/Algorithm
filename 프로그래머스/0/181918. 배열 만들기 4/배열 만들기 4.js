function solution(arr) {
    let i = 0;
    let stk = [];
    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i])
            i += 1
        } else {
            const value = arr[i];
            if (stk.at(-1) < value) {
                stk.push(value)
                i += 1
            } else {
                stk.splice(-1, 1)
            }  
        }
        
    }
    return stk;
}