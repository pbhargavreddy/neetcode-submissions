from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_1  = [0]*26
        freq_2 = [0]*26
        for i in range(len(s)):
            idx_s = ord(s[i])-ord('a')
            idx_t = ord(t[i])-ord('a')
            freq_1[idx_s] += 1
            freq_2[idx_t] += 1
        for i in range(26):
            if freq_2[i] != freq_1[i]:
                return False
        return True