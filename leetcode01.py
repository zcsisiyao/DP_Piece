from collections import deque


class Solution:
    def colorBorder(self, grid, row, col, color):
        originalColor = grid[row][col]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque([(row, col)])
        visited[row][col] = True
        while q:
            x, y = q.popleft()
            isBorder = False
            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                    isBorder = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            if isBorder:
                borders.append((x, y))
        for x, y in borders:
            grid[x][y] = color
        return grid

if __name__=='__main__':
    a = Solution()
    b = a.colorBorder([[1,1,1],[1,1,1],[1,1,1]],1, 1, 2)
    print(b)