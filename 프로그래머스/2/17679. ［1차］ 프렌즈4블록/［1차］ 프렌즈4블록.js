function solution(m, n, board) {
    let answer = 0;
    let array = board.map(row => row.split(''));
    const directions = [[1,0], [0,1], [1,1]];
    
    while (true) {
        let clearArray = new Set();
        
        for (let i = 0; i < m - 1; i++) {
            for (let j = 0; j < n - 1; j++) {
                let character = array[i][j]; 
                if (character === '') continue;
                
                let position = new Set();
                for (let k = 0; k < 3; k++) {
                    let newR = i + directions[k][0], newC = j + directions[k][1];
                    if (
                        array[newR][newC] === character
                    ) {
                        position.add(`(${newR},${newC})`);
                    } else break;
                }
                if (position.size === 3) {
                    clearArray.add(`(${i},${j})`);
                    position.forEach(p => clearArray.add(p));
                }
            }
        }

        if (clearArray.size === 0) break;
        else answer += clearArray.size;

        // 블록 삭제
        clearArray.forEach(p => {
            let [r, c] = p.replace(/[()]/g, '').split(',').map(Number);
            if (array[r][c] !== '') {
                array[r][c] = '';
            }
        });

        // 블록 낙하
        for (let col = 0; col < n; col++) {
            const temp = [];
            for (let row = m - 1; row >= 0; row--) {
                if (array[row][col] !== '') temp.push(array[row][col]);
            }
            for (let row = m - 1; row >= 0; row--) {
                array[row][col] = temp.shift() || '';
            }
        }
    }

    return answer;
}
