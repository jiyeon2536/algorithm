const solution = (price, money, count) => {
    return Math.max((price + (price * count)) * count / 2 - money, 0)
}