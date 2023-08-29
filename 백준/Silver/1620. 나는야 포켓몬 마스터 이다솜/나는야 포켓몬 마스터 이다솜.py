# 나는야 포켓몬 마스터 이다솜
import sys
n, m = map(int, input().split())
pokemon = dict()
cnt = 1
for i in range(n):
    pokemon[sys.stdin.readline().strip()] = cnt
    cnt += 1

r_poket = {v: k for k, v in pokemon.items()}
for j in range(m):
    a = sys.stdin.readline().strip()
    if a.isdigit():
        print(r_poket[int(a)])
    else:
        print(pokemon[a])