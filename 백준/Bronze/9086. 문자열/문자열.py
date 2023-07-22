T = int(input())

for i in range(T):
    my_word = input()
    last_dig = len(my_word) - 1
    print(my_word[0], my_word[last_dig], sep="")