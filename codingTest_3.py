def solution(N):

    if N == 0:
        return 50

    elif N > 0:
        return int(positiveNum(str(N)))

    elif N < 0:
        return int(negativeNum(str(N)[1:]))

# insert 5 before the number less than 5
def positiveNum(N):
    for i, num in enumerate(N):
        if num < '5':
            return N[:i] + '5' + N[i:]
    return N + '5'

# insert 5 after the number less than 5
def negativeNum(N):
    for i, num in enumerate(N):
        if num > '5':
            return '-' + N[:i] + '5' + N[i:]
    return '-' + N + '5'

N = 268
print(solution(N))
