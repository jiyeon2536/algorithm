const intToTern = (num) => {
    let result = '';
    while (num >= 3) {
        result += String(num % 3)
        num = Math.floor(num / 3)
    }
    return result + num
}

const solution = (n) => {
    return parseInt(intToTern(n), 3)
}