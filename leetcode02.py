class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        row_max = []
        col_max = []
        height_val = 0
        for j in range(len(grid)):
            row_max.append(max(grid[j][:]))
            col_max.append(max(grid[:][j]))
        for i in range(len(grid)):
            for j in range(len(grid)):
                height_val = height_val + min(row_max[i], col_max[j]) - grid[i][j]
        return height_val

if __name__=='__main__':
    a = Solution()
    b = a.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
    print(b)