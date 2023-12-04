import sys
input = sys.stdin.readline

di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

tc = int(input())  # 테스트 케이스의 수

for t in range(tc):
    n = int(input())  # 체스판 한 변의 길이

    st_i, st_j = map(int, input().split()) # 나이트 출발 칸
    ed_i, ed_j = map(int, input().split()) # 나이트 목표 칸

    # BFS

    visited = list([0] * n for _ in range(n))
    need_visit = [(st_i, st_j)]
    visited[st_i][st_j] = 1
    # 큐에 쌓아서 앞에부터 뺀다
    while need_visit:
        if visited[ed_i][ed_j] != 0:
            print(visited[ed_i][ed_j] - 1)
            break
        tmp = need_visit.pop(0)
        now_i = tmp[0]
        now_j = tmp[1]
        for k in range(8):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                visited[ni][nj] = visited[now_i][now_j] + 1

                need_visit.append((ni, nj))

    # if visited[ed_i][ed_j] > 0:
    #     print(visited[ed_i][ed_j] -1)
    # else:
    #     print(visited[ed_i][ed_j])