def solution(id_list, report, k):
    answer = {i:0 for i in id_list} # 몇번 연락받는지
    reported = {i:0 for i in id_list}  # 몇번 신고당했는지
    notify = {i:[] for i in id_list}   # 누가 이사람을 신고했는지
    
    for r in report:
        reporter, reportee = r.split(' ')
        if reporter not in notify[reportee]:
            notify[reportee].append(reporter)
            reported[reportee] += 1
    
    for p in reported:
        if reported[p] >= k:
            for n in notify[p]:
                answer[n] += 1
    
    return list(answer.values())