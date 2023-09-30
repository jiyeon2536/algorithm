# 단어 정렬
import sys
input = sys.stdin.readline
n = int(input())
words = []
for i in range(n):
    word = input().strip()
    if [word, len(word)] not in words:
        words.append([word, len(word)])

words = sorted(words, key=lambda x:x[0])
words = sorted(words, key=lambda x:x[1])


for i in range(len(words)):
    print(words[i][0])
