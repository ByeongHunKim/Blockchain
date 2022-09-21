# 사용 전
from sys import stdin

def climb(num):
    score = [stairs[0]]
    if num == 1:
        return score[0]
    score.append(score[0]+stairs[1])
    if num == 2:
        return score[-1]

    score.append(max(stairs[2]+score[0], stairs[2]+stairs[1]))

    for step in range(3,num):
        score.append(max(stairs[step] + stairs[step-1] + score[step-3],stairs[step] + score[step-2]))
    
    return score[-1]

num_stairs = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(num_stairs)]
print(climb(num_stairs))