def solution(N):
    # write your code in Python 2.7
    b = bin(N).split('0b')[1]
    print b
    n = len(b)
    max = 0
    max_l = 0
    start = False
    for i in range(n):
#         print b[i]
        bi = int(b[i])
        if (not start) & (i != n - 1) & (bi == 0):
            continue
        elif (not start) & (i != n - 1) & (bi == 1):
            start = True
        elif start & (i != n - 1) & (bi == 0):
            max_l += 1
        elif start & (i != n - 1) & (bi == 1):
            if max_l > max:
                max = max_l
            max_l = 0
        elif start & (i == n - 1) & (bi == 1):
            if max_l > max:
                max = max_l
                max_l = 0
    return max
# print solution(9) == 2
# print solution(529) == 4
# print solution(20) == 1
print solution(1041) == 5

# print solution(9)
# print solution(529)
# print solution(20)
# print solution(1041)
print solution(74901729)