const solution = (s) => {
    if (s.length !== 6 && s.length !== 4) {
        return false
    }
    for (let i = 0; i < s.length; i++) {
        if (!Number.isInteger(Number(s[i]))) {
            return false
        }
    }
    return true
}