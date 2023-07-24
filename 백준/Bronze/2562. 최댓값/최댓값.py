num_list = []
for i in range(9):
    a = int(input())
    num_list.append(a)

mx = num_list[0]
for j in num_list:
    if j > mx:
        mx = j

print(mx)
print(num_list.index(mx) + 1)