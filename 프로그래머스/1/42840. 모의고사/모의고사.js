function solution(answers) {
    let answer = [];
    const pattern = {
        1 : [1, 2, 3, 4, 5],
        2 : [2, 1, 2, 3, 2, 4, 2, 5],
        3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    
    let score = new Array(3).fill(0)
    
    // 범위 넘어갔을때
    
    for (let i = 0; i < answers.length; i++) {
        const correct = answers[i]
        if (pattern[1][i % pattern[1].length] === correct) score[0] += 1
        if (pattern[2][i % pattern[2].length] === correct) score[1] += 1
        if (pattern[3][i % pattern[3].length] === correct) score[2] += 1
    }
    
    const maxScore = Math.max(...score)
    
    for (let j = 0; j < 3; j++) {
        if (score[j] === maxScore) answer.push(j+1)
    }
    
    console.log(score)
    return answer
}