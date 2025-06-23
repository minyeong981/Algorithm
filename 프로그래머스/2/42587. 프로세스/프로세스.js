function solution(priorities, location) {
    let queue = priorities.map((priority, index) => [priority, index]);
    let answer = 0;

    while (queue.length > 0) {
        let [currentPriority, currentIndex] = queue.shift();
        
        // 뒤에 더 높은 우선순위가 있는지 확인
        if (queue.some(([priority]) => priority > currentPriority)) {
            queue.push([currentPriority, currentIndex]); // 뒤로 보냄
        } else {
            answer += 1; // 실행 처리
            if (currentIndex === location) {
                return answer;
            }
        }
    }
}
