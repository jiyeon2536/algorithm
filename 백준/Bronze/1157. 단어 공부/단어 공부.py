word = input().upper()

no_rep = ''
for m in word:
    if m not in no_rep:
        no_rep += m

cnt_ls = []
for i in no_rep:
    cnt = 0
    for j in range(len(word)):
        if i == word[j]:
            cnt += 1
    cnt_ls.append(cnt)

if cnt_ls.count(max(cnt_ls)) == 1:
    print(no_rep[cnt_ls.index(max(cnt_ls))])
else:
    print('?')