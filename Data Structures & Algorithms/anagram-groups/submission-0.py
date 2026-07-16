from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = []
        res = []
        for i in range(len(strs)):
            if i in seen:
                continue
            path=[strs[i]]
            seen.append(i)
            for j in range(i+1,len(strs)):
                if j in seen:
                    continue
                if self.isAnagram(strs[i],strs[j]):
                    seen.append(j)
                    path.append(strs[j])
            res.append(path)
        return res
            
    def isAnagram(self,a,b):
        if len(a) != len(b):
            return False
        counter1 = Counter(a)
        counter2 = Counter(b)
        return counter1 == counter2