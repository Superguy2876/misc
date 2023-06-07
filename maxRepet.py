from itertools import count


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        c = Counter()
        l = 0
        r = 0
        c[s[r]] += 1
        maxLen = 1
        while r < len(s) - 1:
            
            r += 1
            c[s[r]] += 1

            if c.total() - c.most_common(1)[0][1] > k:
                c[s[l]] -= 1
                l += 1
                
            maxLen = max(maxLen, r - l + 1)
        return maxLen

if __name__ == '__main__':
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))

    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s, k))
