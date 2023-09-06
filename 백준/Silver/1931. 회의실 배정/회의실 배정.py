# 회의실 배정
import sys
n = int(sys.stdin.readline())

timetable = []
# 시작시간, 종료시간
for i in range(n):
    s, e = map(int, sys.stdin.readline().strip().split())
    timetable.append((s, e))

# 종료시간 기준으로 정렬
timetable = sorted(timetable)
timetable = sorted(timetable, key=lambda x: x[1])

cnt = 1
end = timetable[0][1]
for i in range(1, n):
    if timetable[i][0] >= end:
        end = timetable[i][1]
        cnt += 1

print(cnt)