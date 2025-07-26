function solution(arr) {
    let answer = 0;

    while (true) {
        const prev = [...arr];

        arr = arr.map(num => {
            if (num < 50 && num % 2 === 1) {
                return num * 2 + 1;
            } else if (num >= 50 && num % 2 === 0) {
                return num / 2;
            }
            return num;
        });

        const isSame = prev.every((v, i) => v === arr[i]);
        if (isSame) break;
        answer++;
    }

    return answer;
}
