function solution(numbers) {
    var answer = []
    const n = numbers.length
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const tmp = numbers[i] + numbers[j]
            if (!answer.includes(tmp)) {
                answer.push(tmp)
            }
            
        }
    }
    return answer.sort((a, b) => a - b)
}