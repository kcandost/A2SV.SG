class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_rev = s[::-1]
        if s == s_rev:return True
        for i in range(len(s)):
            print(i)
            if s[i] != s_rev[i]:
                s_front = s[:i] + s[i+1:]
                s_end = s_rev[:i] + s_rev[i+1:]
                print(s_front,s_end)
                return s_front == s_front[::-1] or s_end == s_end[::-1]
      
                

