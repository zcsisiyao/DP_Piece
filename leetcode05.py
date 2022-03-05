class Solution:
    def reverseOnlyLetters(self, s):
        dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        news = ""
        nondict = []
        for i in range(len(s)):
            if s[i] not in dictionary:
                nondict.append(i)
            else:
                news += s[i]
        news = news[::-1]
        for i in nondict:
            news = news[:i] + s[i] + news[i:]

        return news
if __name__=='__main__':
    a = Solution()
    b = a.reverseOnlyLetters("Test1ng-Leet=code-Q!")
    print(b)

