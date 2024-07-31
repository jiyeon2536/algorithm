const solution = (x, n) => {
    return Array.from({length : n}, (_, idx) => x * (idx + 1) )
}