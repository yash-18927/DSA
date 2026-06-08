class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        MOD = 10**9 + 7
        req = {end: cnt for end, cnt in requirements}
        max_c = max(req.values())
        if 0 in req and req[0] != 0:
            return 0
        dp = [0] * (max_c + 1)
        dp[0] = 1
        for i in range(1, n):
            new_dp = [0] * (max_c + 1)
            curr = 0
            for j in range(max_c + 1):
                curr += dp[j]
                if j > i:
                    curr -= dp[j - i - 1]
                new_dp[j] = curr % MOD
            dp = new_dp
            if i in req:
                for j in range(max_c + 1):
                    if j != req[i]:
                        dp[j] = 0
        return dp[req[n - 1]] if n - 1 in req else sum(dp) % MOD
