#242. Is Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        SortedS = sorted(s)
        SortedT = sorted(t)
        return SortedS == SortedT