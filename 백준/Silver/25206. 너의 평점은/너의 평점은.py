scores = []
for i in range(20):
    scores.append(list(input().split()))

# 학점 * 과목 평점 / 학점 총합

grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
to_num = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

score_sum = 0
credit_sum = 0
for sub in scores:
    if sub[2] not in grades:
        continue
    else:
        score_sum += float(sub[1]) * float(to_num[grades.index(sub[2])])
        credit_sum += float(sub[1])

print(score_sum / credit_sum)