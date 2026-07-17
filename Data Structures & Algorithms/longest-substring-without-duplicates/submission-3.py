class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 1
        l = r = 0
        freq = [0]*128
        while(l<=r and r<len(s)):
            freq[ord(s[r])] +=1
            while freq[ord(s[r])] > 1:
                freq[ord(s[l])] -=1
                l+=1
            max_length = max(max_length,r-l+1)
            r +=1
        return max_length