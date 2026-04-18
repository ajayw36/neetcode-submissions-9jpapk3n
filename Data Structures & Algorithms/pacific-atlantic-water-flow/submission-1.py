class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(ocean, r, c):
            ocean.add((r, c))
            if (r + 1, c) not in ocean and r + 1 < len(heights) and heights[r + 1][c] >= heights[r][c]:
                dfs(ocean, r + 1, c)
            if (r - 1, c) not in ocean and r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfs(ocean, r - 1, c)
            if (r, c + 1) not in ocean and c + 1 < len(heights[0]) and heights[r][c + 1] >= heights[r][c]:
                dfs(ocean, r, c + 1)
            if (r, c - 1) not in ocean and c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                dfs(ocean, r, c - 1)

        for j in range(len(heights[0])):
            dfs(pacific, 0, j)
        for i in range(len(heights)):
            dfs(pacific, i, 0)
        for j in range(len(heights[0])):
            dfs(atlantic, len(heights) - 1, j)
        for i in range(len(heights)):
            dfs(atlantic, i, len(heights[0]) - 1)

        return [[r, c] for (r, c) in pacific & atlantic]