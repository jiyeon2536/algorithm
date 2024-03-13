function solution(k, tangerine) {
    var answer = 0;
    let numbers = {}
    
    tangerine.forEach((el)=>{
        if (!numbers[el]) {
            numbers[el] = 1
        } else {
            numbers[el] += 1
        }
    })
    
    let values = Object.values(numbers)
    values.sort((a, b) => b- a)

    let len = values.length
    for (let i = 0; i < len; i++) {
        if (k <= 0) {
            break
        }
        k -= values[i]
        answer += 1
    }
    
    return answer;
}