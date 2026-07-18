from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # i need a substring in s2 such that it contains every char in s1.
        # window size is fixed and it is len(s1)

        len1 = len(s1)
        len2 = len(s2)
        if len1>len2:
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for i in range(len1):
            freq1[s1[i]] +=1
            freq2[s2[i]] +=1
        if freq1 == freq2:
            return True
        
        l,r = 0,len1
        while(r<len2):
            freq2[s2[l]] -=1
            if freq2[s2[l]] ==0:
                del freq2[s2[l]]
            l +=1
            freq2[s2[r]] +=1
            r +=1
            if freq1 == freq2:
                return True
        return False
            