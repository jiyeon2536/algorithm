function solution(queue1, queue2) {
    let tried = 0
    const queueLength = queue1.length + queue2.length
    let isFound = false
    let idx1 = 0
    let idx2 = 0
    
    let sum1 = queue1.reduce((acc, cur) => acc + cur)
    let sum2 = queue2.reduce((acc, cur) => acc + cur)

    while (tried < queueLength * 2) {
        if (sum1 > sum2) {
            const elem = queue1[idx1++]
            sum1 -= elem
            sum2 += elem
            queue2.push(elem)
        } else if (sum1 < sum2) {
            const elem = queue2[idx2++]
            sum1 += elem
            sum2 -= elem
            queue1.push(elem)
        } else {
            isFound = true
            break
        }
        tried ++
    }
    
    return isFound ? tried : -1
    
}