function solution(s) {
    let answer = [];
    let dict = {};
    for (let i = 0; i < s.length; i++) {
        s[i] in dict ? answer.push(i - dict[s[i]]) : answer.push(-1);
        dict[s[i]] = i
    }
    return answer;
}