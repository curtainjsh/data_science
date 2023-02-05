def gettotalefficiency(skill):
    skill.sort(reverse=True)
    a,b=[],[]
    p,q = 1,1
    for v in skill:
        if sum(a)<sum(b):
            a.append(v)
        else:
            b.append(v)
    for i in a:
        p *= i
    for j in b:
        q *= j
    return p+q
nums = [1,5,4,2]
a = gettotalefficiency(nums)
a
