function solution(friends, gifts) {
    var answer = 0;
    const n = friends.length
    
    // 개인 선물 지수 오브젝트 생성
    let giftStat = new Object()
    let nextMonth = new Object()
    friends.map((friend) => {
        giftStat[friend] = 0
        nextMonth[friend] = 0
    })
    
    
    
    // 모든 선물지수 오브젝트
    let totalGiftStat = new Object()
    friends.map((friend) => {
        totalGiftStat[friend] = {...giftStat}
    })
        
    // 선물 지수 채우기
    gifts.map((gift) => {
        const [giver, receiver] = gift.split(' ')
        // 개인 내역
        giftStat[giver] += 1
        giftStat[receiver] -= 1
        
        // 전체 내역
        totalGiftStat[giver][receiver] += 1
    })
    
    // console.log(giftStat)
    
    // 이중포문 돌면서 이번달에 선물 몇개 받는지 확인
    for (let i = 0; i < n; i++) {
        const me = friends[i] // 현재 확인할 사람
        for (let j = 0; j < n; j++) {
            const you = friends[j] // 상대

            if (me === you) {
                continue
            } 
            
            const sentAmount = totalGiftStat[me][you]
            const receivedAmount = totalGiftStat[you][me]
            
            // 준 게 더 많으면 하나 받음
            if (receivedAmount < sentAmount) {
                nextMonth[me] += 1
            } else if (receivedAmount === sentAmount) {
                // 준거랑 받은게 같으면 선물 지수를 비교한다.
                if (giftStat[me] > giftStat[you]) {
                    // 내 선물 지수가 크면 하나 받음
                    nextMonth[me] += 1
                }
            }
        }
    }    
    
    const giftAmount = Object.values(nextMonth)
    answer = Math.max(...giftAmount)
    
    return answer;
}