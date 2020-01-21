import numpy as np


def _number():
    return len(scores)


def _max():
    return max(scores)


def _min():
    return min(scores)


def _avg():
    avg = sum(scores)/len(scores)
    return float(avg)


def _std():
    return np.std(scores)


def _median():
    return np.median(scores)


def _sorting():
    b = sorted(scores)
    return b


scores = []
scores_buffer = []
score = 0
count = 0
#while score >=0 and score <= 100:
while 0 <= score <= 100:
    count+=1
    print("Input score(",count,") or -1 to end input : ", end = "")
    score = int(input())
    scores_buffer.append(score)

scores_buffer.pop()
scores = scores_buffer
#print(scores)
print("\nnum of score: ", _number())
print("Max: ", _max())
print("Min: ", _min())
print("Average: ", float(_avg()))
print("Standard deviation: ", _std())
print("Median: ", _median())
print("Sort: ", _sorting())
