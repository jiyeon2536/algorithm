const solution = (s) => {
    let order = 0;
    return ([...s].map((el) => {
        if (el === ' ') {
            order = 0
            return el
        }
        if (order % 2 === 0) {
            order ++;
            return el.toUpperCase()
        } else if (order % 2 === 1) {
            order ++;
            return el.toLowerCase()
        } 
    })).join('')
}