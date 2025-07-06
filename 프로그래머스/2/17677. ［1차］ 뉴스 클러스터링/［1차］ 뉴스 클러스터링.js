function makeValidElements(str) {
    const validMap = new Map();
    let validEleLength = 0;
    const charArray = str.split('');
    for (let i = 0; i < str.length; i++) {
        let ele = charArray.slice(i, i+2).join('').toLowerCase();
        if (/^[a-z]{2}$/.test(ele)) {
            validMap.set(ele, (validMap.get(ele) || 0) + 1);
            validEleLength++;
        }
    }
    return [validMap, validEleLength];
}

function solution(str1, str2) {
    const [s1Map, s1Size] = makeValidElements(str1);
    const [s2Map, s2Size] = makeValidElements(str2);

    if (s1Size === 0 && s2Size === 0) return 65536;
    
    // 교집합 수
    let intersectionCount = 0;
    for (const [key, value] of s2Map) {
        if (s1Map.has(key)) {
            const count = Math.min(s1Map.get(key), value);
            intersectionCount += count;
        }
    }
    
    // 합집합 수
    const unionCount = s1Size + s2Size - intersectionCount;

    return Math.trunc(intersectionCount/unionCount*65536);
}