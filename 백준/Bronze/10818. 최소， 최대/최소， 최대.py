N = int(input())
nums = input().split()
nums_list = []

for i in range(N):
    nums_list.append(int(nums[i]))

mn = nums_list[0]
mx = nums_list[0]

for j in nums_list:
    if j < mn:
        mn = j
    if j > mx:
        mx = j

print(mn, mx)