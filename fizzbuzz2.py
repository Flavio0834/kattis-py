N, M = map(int, input().split())
good_answers = []
for i in range(1, M + 1):
    if i % 3 == 0 and i % 5 == 0:
        good_answers.append("fizzbuzz")
    elif i % 3 == 0:
        good_answers.append("fizz")
    elif i % 5 == 0:
        good_answers.append("buzz")
    else:
        good_answers.append(str(i))

candidates = [0 for i in range(N)]
for i in range(N):
    answers = input().split()
    for j in range(M):
        if answers[j] == good_answers[j]:
            candidates[i] += 1

print(candidates.index(max(candidates)) + 1)
