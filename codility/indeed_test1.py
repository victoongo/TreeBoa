def solution(A):
    # write your code in Python 2.7
    N = len(A)
    # for i in range(N):
    #     print A[i]
    print A
    L = []
    for i in range(N):
        if i == 0:
            L.append(0)
        elif i == 1:
            L.append(A[0])
        else:
            L.append(L[i-1] + A[i-1])
    print L

    U = []
    for i in range(N):
        if i == 0:
            U.append(0)
        elif i == 1:
            U.append(A[N-1])
        else:
            U.append(U[i-1] + A[N-i])
    print U

    U2 = []
    for i in range(N):
        U2.append(U[N-1-i])
    print U2

    for i in range(N):
        if L[i] == U[N-1-i]:
            return i


a = [-1, 3, -4, 5, 1, -6, 2, 1]
print solution(a)