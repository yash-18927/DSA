class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rows = len(img)
        cols = len(img[0])
        smoothed_img = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total_sum = 0
                count = 0
                
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            total_sum += img[nr][nc]
                            count += 1
                
                smoothed_img[r][c] = total_sum // count
                
        return smoothed_img
