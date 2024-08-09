const upperA = 'A'.codePointAt(0)
const lowerA = 'a'.codePointAt(0)

const isUpper = (asc) => {
    if (upperA <= asc && asc <= 'Z'.codePointAt(0)) return true
    return false
}

const solution = (s, n) => {
    let result = '';

    for (let i = 0; i < s.length; i++) {
        const asc = s.charCodeAt(i)
        if (s[i] === ' ') result += s[i]
        else if (isUpper(asc)) {
            result += String.fromCharCode((asc + n - upperA) % 26 + upperA)
        }
        else {
            result += String.fromCharCode((asc + n - lowerA) % 26 + lowerA)
        }
    }
    
    return result
}