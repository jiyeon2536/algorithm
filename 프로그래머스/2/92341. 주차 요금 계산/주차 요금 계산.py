def time_to_min(timestr):
    acc = 0
    # 시간
    hour = int(timestr[:2]) * 60
    acc += hour
    # 분
    minute = int(timestr[3:])
    acc += minute
    return acc


def stay_to_fee(stayed_min, fees):
    accumulated = 0
    root_min, root_fee, plus_min, plus_fee = fees
    if stayed_min <= root_min :
        return root_fee
    else:
        accumulated += root_fee
        stayed_min -= root_min
        # 단위시간으로 나누어진다면
        if stayed_min % plus_min == 0:
            accumulated += (stayed_min // plus_min) * plus_fee
        # 단위시간으로 나누어지지 않는다면
        else:
            accumulated += ((stayed_min // plus_min) + 1) * plus_fee
    return accumulated
        

def solution(fees, records):
    answer = []
    infos = {}
    inout_infos = {}
    
    for record in records:
        time, car_num, in_out = record.split(' ')
        if in_out == 'IN':
            inout_infos[car_num] = False
            # 입차시
            if car_num in infos:  # 이미 오늘 다녀갔다면
                infos[car_num].append(time_to_min(time))
            else: # 오늘 처음으로 왔으면
                infos[car_num] = [time_to_min(time)]
        else:
            inout_infos[car_num] = True
            # 출차시간 - 입차시간 pop하여 체류시간 넣고 다시 append
            stayed_min = time_to_min(time) - infos[car_num].pop()        
            infos[car_num].append(stayed_min)

    # 다 돌았는데 출차하지 않았다면
    cars = list(infos.keys())
    for car in cars:
        if inout_infos[car] == False:
            stayed_min = time_to_min('23:59') - infos[car].pop()
            infos[car].append(stayed_min)
    
        
    for i in infos:
        infos[i] = stay_to_fee(sum(infos[i]), fees)
    
    
    sorted_keys = sorted(cars)
    for key in sorted_keys:
        answer.append(infos[key])
    
    return answer