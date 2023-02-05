import bisect
def locate(mat,target):
    meta = [lst[-1] for lst in mat]
    i1 =bisect.bisect_left(meta,target)

    if i1 != len(meta):
        lst = mat[i1]
        i2 = bisect.bisect_left(lst,target)
        if i2 != len(lst) and lst[i2] == target:
            return(i1,i2)
        return -1


