from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 현재 초수 저장
    clock = 0
    
    bridge = deque()  # bridge에 올라와있는 차
    waiting = deque(truck_weights)
    
    cur_weight = 0
    
    while waiting:  # 대기하는 차가 있는 동안..
        clock += 1
        # 맨 앞 친구가 빠질 수 있는지 확인하고 뺌.
        if bridge and (clock - bridge[0][1] >= bridge_length):
            passed = bridge.popleft()
            cur_weight -= passed[0]
        
        if cur_weight + waiting[0] <= weight and len(bridge) < bridge_length:
            now = waiting.popleft()  # 대기하는 친구가
            bridge.append((now, clock))  # 다리위로 올라간다
            cur_weight += now # 지금 다리 위 무게
    
    # 이제 대기하던 차는 다 올라옴.
    # 그러면 다리에 올라와 있는 거 중에 가장 마지막 아이가 건널 초를 더해주면 됨
    clock += bridge_length - (clock - bridge[-1][1])
    
    return clock