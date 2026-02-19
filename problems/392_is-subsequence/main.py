class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0 , len(t)-1
        n = len(s)
        s1 = 0
        if n == 0:
            return True
        while i <= j:
            if t[i] != s[s1]:
                i += 1
            else:
                i+=1
                s1+=1
            if s1 == n:
                return True
        return False

        


if __name__ == "__main__":
    samples = [
        {"s": "abc", "t": "ahbgdc", "expected": True},
        {"s": "axc", "t": "ahbgdc", "expected": False},
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        result = solver.isSubsequence(sample["s"], sample["t"])
        print(f"Sample {i} result: {result}")
        print(f"Sample {i} expected: {sample['expected']}")
