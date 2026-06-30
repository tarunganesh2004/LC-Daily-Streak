# Number of Substrings containing all three characters LC 1358

s="abcabc"

def numberOfSubstrings(s):
    n=len(s)
    count=0

    char_count={'a':0,'b':0,'c':0}
    left=0
    for right in range(n):
        char_count[s[right]]+=1
        print(char_count,right)

        while char_count['a']>0 and char_count['b']>0 and char_count['c']>0:
            count+=(n-right)
            print(count)

            char_count[s[left]]-=1
            left+=1
        print(left)
    return count

print(numberOfSubstrings(s))