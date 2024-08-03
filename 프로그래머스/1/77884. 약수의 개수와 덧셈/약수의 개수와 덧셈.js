const solution = (left, right) => {
    let result = 0;
    for (let i = left; i <= right; i++) {
        if (Math.sqrt(i) % 1 === 0) {
            result -= i
        } else {
            result += i
        }
    }
    return result
}