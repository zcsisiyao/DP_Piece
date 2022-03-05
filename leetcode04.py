class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            b = s[:i + 1]
            n = (len(s) // len(b))
            if b * n == s:
                return True
        return False

if __name__=='__main__':
    a = Solution()
    b = a.repeatedSubstringPattern("aba")
    print(b)