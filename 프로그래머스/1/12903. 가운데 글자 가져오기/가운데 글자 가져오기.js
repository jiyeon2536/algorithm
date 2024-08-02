const solution = (s) => {
    const half = Math.floor(s.length / 2)
    return s.length % 2 ? s[half] : s.slice(half - 1, half + 1)
}