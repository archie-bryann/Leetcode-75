from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        queue = deque()
        queue.append((sr, sc))

        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    queue.append((nr, nc))

        return image