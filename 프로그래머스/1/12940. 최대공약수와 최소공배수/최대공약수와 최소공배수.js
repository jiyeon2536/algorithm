const gcd = (n, m) => {
    const smaller = Math.min(n, m)
    for (let i = smaller; i > 0; i--) {
        if (n % i === 0 && m % i === 0) {
            return i
        }
    }
}

const lcm = (n, m) => {
    const bigger = Math.max(n, m)
    for (let i = bigger; i <= n * m; i++) {
        if (i % n === 0 && i % m === 0) {
            return i
        }
    }
}

const solution = (n, m) => {
    return [gcd(n, m), lcm(n, m)]
}