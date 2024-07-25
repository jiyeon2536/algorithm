function solution(people, limit) {
    let ship = people.length
    
    people.sort((a, b) => a - b)
    
    let first = 0
    let last = ship - 1
    
    while (first < last) {
        if (people[first] + people[last] <= limit) {
            ship -= 1
            first += 1
        }
        last -= 1
    }
    
    return ship;
}