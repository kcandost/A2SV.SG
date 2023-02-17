class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for c in s:
            if c in hash:
                hash[c]+=1
            else:
                hash.update({c:0})
        print(hash)

        for key in hash:
            if hash[key]==0:
                return s.find(key)
        return -1
