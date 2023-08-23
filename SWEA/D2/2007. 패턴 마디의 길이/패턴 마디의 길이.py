# 패턴 마디
t = int(input())

for tc in range(1, t+1):
    s = input()

    pattern = s[0]
    found = 0
    for j in range(1, len(s)):
        if found == 1:
            break
        if s[j] == pattern[0]:
            pattern = s[:j]
            i = 1
            while found == 0:
                tmp = s[j:j + len(pattern)]
                if tmp != pattern:      # 패턴이 아니라면, 다시 찾아?
                    break
                else:                   # 맞으면.. 나가?
                    found = 1

    print(f'#{tc} {len(pattern)}')