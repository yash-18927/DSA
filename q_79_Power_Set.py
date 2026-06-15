class Solution:
    def AllPossibleStrings(self, s: str) -> list[str]:
        result = []
        n = len(s)
        
        def solve(index, current):
            if index == n:
                if current:
                    result.append(current)
                return
            
            solve(index + 1, current + s[index])
            solve(index + 1, current)
            
        solve(0, '')
        result.sort()
        return result
