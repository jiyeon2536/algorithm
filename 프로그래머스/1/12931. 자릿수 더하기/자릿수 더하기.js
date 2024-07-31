const solution = (N) => {
    let answer = 0;
    const n = N.toString()
    for (let i = 0; i < n.length; i++) {
        answer += +n[i];
    }
    return answer
}