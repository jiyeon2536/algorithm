N = int(input())

words = []
for i in range(N):
    words.append(input())

# 전에 나왔는지 안나왔는지 어떻게 알지
# 나왔던 알파벳을 넣어두고
# 해당 알파벳과 이미 나왔던 알파벳이 있으면 그 알파벳의 위치가 -1인지 확인하고
# 아니면 틀린거

cnt = N
for word in words:
    stack = [word[0]]
    for c in range(1, len(word)):
        if word[c] in stack and stack[-1] != word[c]:
            cnt -= 1
            break
        else:
            stack.append(word[c])

print(cnt)