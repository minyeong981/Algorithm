function solution(cacheSize, cities) {
    if (cacheSize === 0) return cities.length * 5;

    let totalTime = 0;
    let cache = [];

    for (let city of cities) {
        city = city.toLowerCase();

        const hitIndex = cache.indexOf(city);

        if (hitIndex !== -1) {
            // Cache hit
            totalTime += 1;
            // 최근 사용했으므로 맨 뒤로 이동
            cache.splice(hitIndex, 1);
            cache.push(city);
        } else {
            // Cache miss
            totalTime += 5;
            if (cache.length >= cacheSize) {
                cache.shift(); // 가장 오래된 것 제거
            }
            cache.push(city);
        }
    }

    return totalTime;
}
