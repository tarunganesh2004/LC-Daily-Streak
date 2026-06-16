# Process String with Special Operations I LC 3612

s="a#b%*"

def processStr(s):
    res=[]
    for ch in s:
        if ord(ch)>=97 and ord(ch)<=128:
            res.append(ch)
        elif ch=='#':
            res=res*2
        elif ch=='%':
            res=res[::-1]
        else:
            res=res[:len(res)-1]
    return ''.join(res)

print(processStr(s))