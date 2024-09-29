function solution(name, yearning, photo) {
    let answer = [];
    let score = {}
    for (let i = 0; i < name.length; i++) {
        score[name[i]] = yearning[i]
    }
    
    for (const ppl of photo) {
        let currentScore = 0;
        for (const person of ppl) {
            person in score ? currentScore += score[person] : currentScore += 0
        }
        answer.push(currentScore)
    }
    
    return answer;
}