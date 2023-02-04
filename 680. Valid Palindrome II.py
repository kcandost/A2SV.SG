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
            
            
"""
1) First we check if it's a palindrome
2) Then we start checking if the opposite ends are the same, until we find a mismatch.
3) When we find the mismatch we check if we can obtain a palindrome from either side, by removing the element we are at.
4) if in either direction we find a palindrome, it returns True
5) if neither is a palindrome, it means the string cannot be turned into a palindrome by moving at most one element, 
and it returns false, since both of those equality statements are false  (return false or false)
"""
      
                

