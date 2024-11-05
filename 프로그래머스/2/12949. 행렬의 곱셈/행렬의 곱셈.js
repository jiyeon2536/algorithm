function matMul(m1, m2) {
    const result = []
    
    for (let i = 0; i < m1.length; i++) {
        result[i] = []
        for (let j = 0; j < m2[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < m1[0].length; k++) {
                sum += m1[i][k] * m2[k][j]
            }
            result[i][j] = sum
        }
    }
    return result
}

function solution(...matrices) {
    let result = matrices[0]
    
    for (let i = 1; i < matrices.length; i++) {
        result = matMul(result, matrices[i])
    }
    
    return result;
}