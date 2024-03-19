function solution(s) {
    let answer = '';
    let arr = Array(...s)
    const len = s.length
    
    for (let i = 0; i < len - 1; i++) {
        if (s[i] === ' ') {
            arr[i+1] = s[i+1].toUpperCase()
        } else {
            arr[i+1] = s[i+1].toLowerCase()
        }
    }
    
    arr[0] = s[0].toUpperCase()


    answer = arr.join('')
    
    return answer;
}