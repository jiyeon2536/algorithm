function solution(s) {
    let answer = '';
    const arr = s.split(' ').map(Number)
    const min = Math.min(...arr)
    const max = Math.max(...arr)
    answer = `${min} ${max}`
    return answer;
}