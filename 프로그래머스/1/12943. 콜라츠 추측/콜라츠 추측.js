const solution = (n) => {
    let result = 0
    while (n !== 1) {
        if (result === 500) {
            return -1;
        }
        if (n % 2 === 0) {
            n /= 2
        } else {
            n = n * 3 + 1
        }
        result++;
    }
    return result;
}