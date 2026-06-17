# Process String With Special Operations II LC 3614

s="a#b%*"
k=1

def processStr(s,k):
    lengths=[]
    cur=0

    # forward pass
    for ch in s:
        if ch.islower():
            cur+=1
        elif ch=='*':
            if cur>0:
                cur-=1
        elif ch=='#':
            cur*=2
        elif ch=='%':
            pass 
        
        lengths.append(cur)

    # edge case 
    if k>=cur:
        return '.'
    
    # backward pass
    for i in range(len(s)-1,-1,-1):
        ch=s[i]
        prev=lengths[i-1] if i>0 else 0
        cur=lengths[i]

        if ch.islower():
            if k==cur-1:
                return ch 
        
        elif ch=='#':
            k%=prev 
        
        elif ch=='%':
            k=cur-1-k 

        elif ch=='*':
            pass 
    
    return '.'

print(processStr(s,k))