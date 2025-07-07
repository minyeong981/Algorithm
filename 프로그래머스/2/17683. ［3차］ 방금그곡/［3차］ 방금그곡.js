function normalize(melody) {
    return melody
        .replace(/C#/g, 'c')
        .replace(/D#/g, 'd')
        .replace(/F#/g, 'f')
        .replace(/G#/g, 'g')
        .replace(/A#/g, 'a')
        .replace(/B#/g, 'b');
}

function getPlayTime(start, end) {
    const [sh, sm] = start.split(':').map(Number);
    const [eh, em] = end.split(':').map(Number);
    return (eh * 60 + em) - (sh * 60 + sm);
}

function makeMelodies(melody, time) {
    let result = '';
    const len = melody.length;
    for (let i = 0; i < time; i++) {
        result += melody[i % len];
    }
    return result;
}

function solution(m, musicinfos) {
    const normalizedM = normalize(m);
    const candidates = [];

    musicinfos.forEach((info, index) => {
        const [start, end, title, sheet] = info.split(',');
        const playTime = getPlayTime(start, end);
        const normalizedSheet = normalize(sheet);
        const fullMelody = makeMelodies(normalizedSheet, playTime);

        if (fullMelody.includes(normalizedM)) {
            candidates.push({ title, playTime, index });
        }
    });

    if (candidates.length === 0) return "(None)";

    candidates.sort((a, b) => {
        if (b.playTime !== a.playTime) return b.playTime - a.playTime;
        return a.index - b.index;
    });

    return candidates[0].title;
}
