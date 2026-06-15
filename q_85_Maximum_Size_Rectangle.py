class Solution:
    def maxArea(self, M: list[list[int]], n: int, m: int) -> int:
        def max_histo(heights):
            stack = []
            max_area = 0
            idx = 0
            while idx < len(heights):
                if not stack or heights[idx] >= heights[stack[-1]]:
                    stack.append(idx)
                    idx += 1
                else:
                    top = stack.pop()
                    width = idx if not stack else idx - stack[-1] - 1
                    max_area = max(max_area, heights[top] * width)
            while stack:
                top = stack.pop()
                width = idx if not stack else idx - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
            return max_area

        if not M:
            return 0
            
        heights = [0] * m
        max_rect = 0
        for i in range(n):
            for j in range(m):
                if M[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_rect = max(max_rect, max_histo(heights))
            
        return max_rect
