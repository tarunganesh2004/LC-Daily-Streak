# LC 2161 Partition Array According to Given pivot

nums=[9,12,5,10,14,3,10]
pivot=10

def pivotArray(nums,pivot):
    l,e,m=[],[],[]
    for num in nums:
        if num<pivot:
            l.append(num)
        elif num==pivot:
            e.append(num)
        else:
            m.append(num)

    return l+e+m 

print(pivotArray(nums,pivot))