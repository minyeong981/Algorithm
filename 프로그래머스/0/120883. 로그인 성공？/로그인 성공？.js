function solution(id_pw, db) {
    var answer = '';
    for (let data of db) {
        if (id_pw[0] === data[0] && id_pw[1] === data[1]) {
            return 'login'
        } else if (id_pw[0] === data[0] && id_pw[1] !== data[1]) {
            answer = 'wrong pw'
        }
    }
    
    if (answer === 'wrong pw') {
        return answer
    } else {
        return 'fail'
    }
}