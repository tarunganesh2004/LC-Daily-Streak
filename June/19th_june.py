# Find the Highest altitude

gain=[-5,1,5,0,-7]

def largestAltitude(gain):
    n=len(gain)
    res=[0]*(n+1)

    for i in range(1,n+1):
        res[i]=gain[i-1]+res[i-1]
    return res,max(res)

print(largestAltitude(gain))