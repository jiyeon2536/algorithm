function solution(bandage, health, attacks) {
    var answer = 0;
    
    // 1초부터 시작해서 attacks의 마지막의 [0]까지
    // 초를 순회하면서 해당 초에 attack 이 있으면 -어택
    // 어택이 없으면 연속 +1 하고 체력 +변화량
    // 연속이 연속량을 꽉 채우고 어택이 없으면 +변화량 +보너스
    
    const lenAttacks = attacks.length
    const lastAttack = attacks[lenAttacks - 1][0]
    let hp = health
    let bandSec = 0
    // 최대시간: bandage[0] 충전량 : bandage[1] 보너스 : bandage[2]
    let attackOrder = 0
    for (let i = 0; i <= lastAttack; i++){
        if (i === attacks[attackOrder][0]) {            
           hp -= attacks[attackOrder][1] 
            if (hp <= 0) {
                return -1
            }
            bandSec = 0
            attackOrder += 1
        } else {
            bandSec ++
            hp += bandage[1]
            if (bandSec === bandage[0]) {
                hp += bandage[2]
                bandSec = 0
            }
            if (hp > health) {
                hp = health
            }
        }
    }   
    
    answer = hp
    
    return answer;
}