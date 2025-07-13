function solution(a, b, c, d) {
    let answer = 0;
    const numbers = [a, b, c, d];
    const dictionary = new Map();
    dictionary.set(1, 0);
    dictionary.set(2, 0);
    dictionary.set(3, 0);
    dictionary.set(4, 0);
    dictionary.set(5, 0);
    dictionary.set(6, 0);
    
    numbers.forEach(num => dictionary.set(num, dictionary.get(num) + 1));
    
    const oneCount = [];
    const twoCount = [];
    const threeCount = [];
    for (const [dice, value] of dictionary.entries()) {
        if (value === 1) oneCount.push(dice);
        if (value === 2) twoCount.push(dice);
        if (value === 3) threeCount.push(dice);
        if (value === 4) return 1111 * dice;
    }

    switch (oneCount.length) {
        case 1 : answer = Math.pow(10 * threeCount[0] + oneCount[0], 2); break;
        case 2 : answer = (twoCount.length === 1) ? (oneCount[0] * oneCount[1]) : 0; break;
        case 4 : answer = oneCount[0]; break;
    }

    return answer === 0 ? (twoCount[0] + twoCount[1]) * Math.abs(twoCount[0] - twoCount[1]) : answer;
}