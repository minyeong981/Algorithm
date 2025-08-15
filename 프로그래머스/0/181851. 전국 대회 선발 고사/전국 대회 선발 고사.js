function solution(rank, attendance) {
    const abc = [];
    const len = rank.length;
    for (let i=1; i <= len; i++) {
        const idx = rank.indexOf(i);
        if (attendance[idx]) {
            abc.push(idx)
        }
        if (abc.length === 3) {
            break;
        }
    }
    
    
    return 10000*abc[0] + 100*abc[1] + abc[2];
}