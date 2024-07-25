def solution(people, limit):
    ship = len(people)
    
    people.sort()
    
    first = 0
    last = len(people) - 1
    
    while first < last:
        if people[first] + people[last] <= limit:
            ship -= 1
            first += 1
        last -= 1
        
    return ship