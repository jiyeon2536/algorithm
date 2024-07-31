const solution = (x, n) => {
    return Array.from({length : n, '0' : x}, (el, idx) => x * (idx + 1) )
}