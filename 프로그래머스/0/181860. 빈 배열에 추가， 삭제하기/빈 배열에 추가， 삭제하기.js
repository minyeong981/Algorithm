function solution(arr, flag) {
    const x = [];
    for (let i=0; i < arr.length; i++) {
        if (flag[i]) {
            for (let j=0; j < arr[i]*2; j++) {
                x.push(arr[i]);
            }
        } else {
            for (let j=0; j < arr[i]; j++) {
                x.pop();
            }
        }
    }
    return x;
}