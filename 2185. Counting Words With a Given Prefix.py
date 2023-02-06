class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        l=len(pref)
        for word in words:
            count+=word[:l]==pref

        return count
