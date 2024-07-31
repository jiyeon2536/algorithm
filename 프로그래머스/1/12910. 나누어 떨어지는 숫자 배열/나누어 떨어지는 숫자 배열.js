const solution = (arr, divisor) => {
    let answer = [];
    arr.forEach((el) => {
        if (el % divisor === 0) answer.push(el)
    })
    return answer.length ? answer.sort((a, b) => a-b) : [-1];
}