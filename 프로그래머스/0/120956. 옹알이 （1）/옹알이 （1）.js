function solution(babbling) {
    const pron = ["aya", "ye", "woo", "ma"];
    let answer = 0;

    for (const bab of babbling) {
        let word = bab;
        let prev = "";   
        let valid = true;

        do {
            let matched = false;

            for (const p of pron) {
                // 앞에서부터 발음이 맞고, 직전 발음과 다르면 처리
                if (word.startsWith(p) && p !== prev) {
                    word = word.slice(p.length);
                    prev = p;
                    matched = true;
                    break; // pron 루프 탈출
                }
            }

            // pron 전부 돌았는데 매칭 안 된 경우 → 불가능
            if (!matched) {
                valid = false;
                break;
            }
        } while (word.length > 0);

        if (valid && word.length === 0) {
            answer++;
        }
    }

    return answer;
}
