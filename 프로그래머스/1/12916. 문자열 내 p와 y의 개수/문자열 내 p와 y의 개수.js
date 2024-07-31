const solution = (s) => {
    let countP = 0
    let countY = 0
    for (let i = 0; i < s.length; i++) {
        if (s.toLowerCase()[i] === 'p') {
            countP ++;
        } else if (s.toLowerCase()[i] === 'y') {
            countY ++;
        }
    }
    
    return countP === countY ? true : false
}