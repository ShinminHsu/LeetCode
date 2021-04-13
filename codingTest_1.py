def solution(N):
    # write your code in Python 3.6
    for i in range(1, N + 1):

        s = ""
        divisible = False  # to check whether the number is divisible by 2, 3 or 5

        #
        if i % 2 == 0:
            divisible = True
            s += "Codility"

        if i % 3 == 0:
            divisible = True
            s += "Test"

        if i % 5 == 0:
            divisible = True
            s += "Coders"

        # if the number can be divided by 2, 3, or 5
        if divisible:
            print(s, end='\n')
        else:
            print(i, end='\n')

solution(24)
