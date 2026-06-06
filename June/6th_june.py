# LC 2574

def leftRightDifference(nums):
    n=len(nums)
    ls=[0]*n 
    for i in range(1,n):
        ls[i]=ls[i-1]+nums[i-1]
    rs=[0]*n 
    for i in range(n-2,-1,-1):
        rs[i]=rs[i+1]+nums[i+1]
    
    ans=[0]*n 
    for i in range(n):
        ans[i]=abs(ls[i]-rs[i])
    return ans 

# spaceoptimized
def another(nums):
    total=sum(nums)
    left=0
    ans=[]
    for num in nums:
        total-=num 
        ans.append(abs(total-left))
        left+=num 
    return ans

nums=[10,4,8,3]
print(leftRightDifference(nums))
print(another(nums))