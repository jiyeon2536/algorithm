function solution(s){
    let answer = true;
    let stack = new Array();

    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            stack.push("(")
        } else if (s[i] === ")") {
            if (stack.length < 1) {
                return false
            }
            else if (stack.length > 0) {
                if (stack[stack.length - 1] === '(') {
                    stack.pop()
                }
                else {
                    return false
                }
            }
        }
    }
    
    return stack.length > 0 ? false : true;
}