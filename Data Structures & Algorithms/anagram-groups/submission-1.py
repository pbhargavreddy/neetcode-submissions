from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = [0]*len(strs)
        for i in range(len(strs)):
            if seen[i] == 1:
                continue
            seen[i] = 1
            path = [strs[i]]
            for j in range(i+1,len(strs)):
                if seen[j]:
                    continue
                if self.isAnagram(strs[i],strs[j]):
                    path.append(strs[j])
                    seen[j] = 1
            res.append(path.copy())
        return res
    def isAnagram(self,s1,s2):
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)