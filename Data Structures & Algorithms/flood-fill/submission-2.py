class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if color == original_color: return image

        q = deque()
        image[sr][sc] = color
        q.append((sr, sc))
        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= r + dr < len(image) and 0 <= c + dc < len(image[0]) and image[r + dr][c + dc] == original_color:
                    image[r + dr][c + dc] = color
                    q.append((r + dr, c + dc))
        return image