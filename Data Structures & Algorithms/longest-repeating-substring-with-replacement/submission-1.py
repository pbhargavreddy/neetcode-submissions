from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_len = 0
        l = r = 0
        max_freq = 0
        # i need maximum substring that has atmost k+1 distinct elements
        while(l<=r and r<len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq,freq[s[r]])
            while(r-l+1 - max_freq > k):
                freq[s[l]] -=1
                l +=1
            max_len = max(max_len,r-l+1)
            r +=1
        return max_len