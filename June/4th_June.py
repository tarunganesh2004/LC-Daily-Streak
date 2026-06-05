# Total Waviness of Numbers in Range I LC 3751

num1=120
num2=130

def totalwaviness(num1,num2):
    def findWaviness(num):
        w=0
        s=str(num)
        n=len(s)
        if n<3:
            return 0
        
        for i in range(1,n-1):
            if s[i]>s[i-1] and s[i]>s[i+1]:
                w+=1
            elif s[i]<s[i-1] and s[i]<s[i+1]:
                w+=1
        return w 
    
    c=0
    for i in range(num1,num2+1):
        c+=findWaviness(i)
    return c

print(totalwaviness(num1,num2))
