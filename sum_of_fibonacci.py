def findfibonaccisum(nums):
    def createHash(hash1,maxElement):
        prev , curr = 0 , 1
        hash1.add(prev)
        hash1.add(curr)
        while (curr < maxElement):
            temp = curr + prev
            hash1.add(temp)
            prev = curr
            curr = temp
        return hash1
    def findFibonacciPair(n):
        hash1 = set()
        hash1 = createHash(hash1, n)
        for i in range(n):
            if (i in hash1 and (n - i) in hash1):
                print(i , ", ", (n - i))
                return True
        return False
    res = []
    for i, num in enumerate(nums):
        res.append(findFibonacciPair(num))
    return res
