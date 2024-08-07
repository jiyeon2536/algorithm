const solution = (sizes) => {
    let mBig = 0
    let mSmall = 0
    sizes.forEach((el) => {
        const bigger = Math.max(...el)
        const smaller = Math.min(...el)
        mBig = Math.max(bigger, mBig)
        mSmall = Math.max(smaller, mSmall)
    })
    return mBig * mSmall
}