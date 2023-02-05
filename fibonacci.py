def solution(x):
    first = 0
    second = 1
    leftFib = 0
    rightFib = 0
    while (True):
        fib = first + second
        first = second
        second = fib
        if (fib < x):
            leftFib = fib
        else:
            rightFib = fib
            break

    if ((x - leftFib) < (rightFib - x)):
        return x - leftFib
    else:
        return rightFib - x


x = 13
res = solution(x)
