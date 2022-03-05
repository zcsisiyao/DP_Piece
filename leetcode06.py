class Solution:
    def maximumRequests(self, n: int, requests):
        buildnumber = [0] * n
        for i in requests:
            buildnumber[i[0]] -= 1
            buildnumber[i[1]] += 1
        unbuildnumber = []
        for i in range(n):
            if buildnumber[i] != 0:
                unbuildnumber.append(i)
        number = 0
        for i in requests:
            for j in unbuildnumber:
                if j in i:
                    number += 1
                    break
        return abs(len(requests) - number)

if __name__=='__main__':
    a = Solution()
    b = a.maximumRequests(3, [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]])
    print(b)
