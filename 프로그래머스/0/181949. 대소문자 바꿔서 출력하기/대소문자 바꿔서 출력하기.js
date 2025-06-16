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
}).on('close', function(){
    console.log(answer);
});
