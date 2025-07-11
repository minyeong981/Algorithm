function solution(msg) {
    const dictionary = new Map();
    const answer = [];

    // A-Z 초기화 (1부터 시작)
    for (let i = 1; i <= 26; i++) {
        dictionary.set(String.fromCharCode(64 + i), i);
    }

    let i = 0;
    let dictSize = 27;

    while (i < msg.length) {
        let w = msg[i];
        while (i + 1 < msg.length && dictionary.has(w + msg[i + 1])) {
            w += msg[++i];
        }

        answer.push(dictionary.get(w));

        if (i + 1 < msg.length) {
            dictionary.set(w + msg[i + 1], dictSize++);
        }

        i++;
    }

    return answer;
}
