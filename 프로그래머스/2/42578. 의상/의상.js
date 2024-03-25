function solution(clothes) {
    let answer = 1
    const n = clothes.length
    let clothesType = {}
    // 옷 개수 
    for (let i = 0; i < n ; i++) {
        const ci = clothes[i][1]
        if (clothesType[ci]) {
        clothesType[ci] += 1           
        } else {
            clothesType[ci] = 1
        }
    }
    
    
    for (let [ty, nu] of Object.entries(clothesType)) {
         answer *= (nu + 1)
    }

    answer -= 1    
    return answer
}