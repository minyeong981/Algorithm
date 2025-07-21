function solution(arr) {
    const firstIndex = arr.indexOf(2);
    const answer = [];
    const isTwoIndexArray = [];
    for (const idex in arr) {
        if (arr[idex] === 2) {
            isTwoIndexArray.push(idex)
        }
    }
    console.log(isTwoIndexArray)
    switch (isTwoIndexArray.length) {
        case 0 : return [-1]; break;
        case 1 : return [arr[isTwoIndexArray.pop()]];break;
        default : return arr.filter((num, i) => i >= isTwoIndexArray.at(0) && i <= isTwoIndexArray.at(-1));
    }
}