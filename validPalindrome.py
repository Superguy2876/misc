class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c for c in s if c.isalnum()).lower()
        count_up = 0
        count_down = len(clean_s) - 1
        while count_up < count_down:
            if clean_s[count_up] != clean_s[count_down]:
                return False
            count_up += 1
            count_down -= 1
        return True