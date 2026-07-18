from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # i need to find a substring that has all chars in t.
        #the substring may have extra chars too.
        if len(t) > len(s):
            return ""

        freq = [0] * 128

        for ch in t:
            freq[ord(ch)] += 1

        l = 0
        count = 0

        start = 0
        min_len = float("inf")

        for r in range(len(s)):
            freq[ord(s[r])] -= 1

            if freq[ord(s[r])] >= 0:
                count += 1

            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                freq[ord(s[l])] += 1

                if freq[ord(s[l])] > 0:
                    count -= 1

                l += 1

        return "" if min_len == float("inf") else s[start:start + min_len]