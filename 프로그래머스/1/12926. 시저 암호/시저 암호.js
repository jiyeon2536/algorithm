const isUpper = (ch) => {
    if ('A'.codePointAt(0) <= ch.charCodeAt(0) && ch.charCodeAt(0) <= 'Z'.codePointAt(0)) return true
    return false
}

const solution = (s, n) => {
    let result = '';
    const upperA = 'A'.codePointAt(0)
    const lowerA = 'a'.codePointAt(0)
    
    for (let i = 0; i < s.length; i++) {
        const asc = s.charCodeAt(i)
        if (s[i] === ' ') result += s[i]
        else if (isUpper(s[i])) {
            result += String.fromCharCode((asc + n - upperA) % 26 + upperA)
        }
        else {
            result += String.fromCharCode((asc + n - lowerA) % 26 + lowerA)
        }
    }
    
    return result
}