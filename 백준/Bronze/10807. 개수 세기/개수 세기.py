N = int(input())
nums = input().split()
nums_list = []


for i in range(N):
    nums_list.append(int(nums[i]))

v = int(input())

cnt = 0
for j in range(N):
    if v == nums_list[j]:
        cnt += 1


print(cnt)