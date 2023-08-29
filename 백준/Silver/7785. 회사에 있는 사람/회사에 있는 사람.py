# easy work
import sys
n = int(sys.stdin.readline())
giigle = {}
for i in range(n):
    name, status = sys.stdin.readline().split()
    giigle[name] = status
t = list(giigle.keys())
present = []
for k in t:
    if giigle[k] != 'leave':
        present.append(k)

present.sort(reverse=True)
for _ in range(len(present)):
    print(present[_])