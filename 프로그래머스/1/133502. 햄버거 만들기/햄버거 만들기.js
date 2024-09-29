function solution(ingredient) {
    let answer = 0;
    let stk = []
    
    for (const ing of ingredient) {
        stk.push(ing)
        if (stk.at(-4) === 1 && stk.at(-3) === 2 && stk.at(-2) === 3 && stk.at(-1) === 1) {
            answer += 1
            stk.pop()
            stk.pop()
            stk.pop()
            stk.pop()     
        }
    }
    
    return answer;
}