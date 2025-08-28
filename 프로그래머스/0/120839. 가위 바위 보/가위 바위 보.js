function solution(rsp) {
    const game = {'2': '0', '0': '5', '5': '2'};
    return rsp.split('').reduce((acc, cur) => acc + game[cur], '');
}