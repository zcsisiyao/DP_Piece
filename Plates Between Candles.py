"""
2055.There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r
        
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]
        return ans
