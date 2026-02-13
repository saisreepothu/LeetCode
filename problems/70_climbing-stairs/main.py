class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    samples = [
        {"n": 2, "expected": 2},
        {"n": 3, "expected": 3},
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        result = solver.climbStairs(sample["n"])
        print(f"Sample {i} result: {result}")
        print(f"Sample {i} expected: {sample['expected']}")
