def palindrome(s:str):
    for i in range(0, len(s)):
        z = (i+1)*-1
        if (s[i] is not s[z]):
            return False
        if i >= len(s)/2:
            return True
    return True

import sys

if (len(sys.argv) > 1):
    print(palindrome(sys.argv[1]))
