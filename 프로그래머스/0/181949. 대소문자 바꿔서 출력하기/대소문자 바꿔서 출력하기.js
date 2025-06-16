const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let answer = '';

rl.on('line', function (line) {
    for (let char of line) {
        if (char === char.toUpperCase()) {
            answer += char.toLowerCase();
        } else {
            answer += char.toUpperCase();
        }
    }
    console.log(answer);
    rl.close();
}).on('close', function(){
});
