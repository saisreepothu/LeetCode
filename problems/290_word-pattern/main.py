class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        if len(pattern) != len(ss):
            return False
        c2w = {}
        w2c = {}
        
        for c, w in zip(pattern, ss):
            if c in c2w and c2w[c] != w:
                return False
            if w in w2c and w2c[w] != c:
                return False
            if c not in c2w or w not in w2c:
                c2w[c] = w
                w2c[w] = c 
        return True


if __name__ == "__main__":
    samples = [
        {"pattern": "abba", "s": "dog cat cat dog", "expected": True},
        {"pattern": "abba", "s": "dog cat cat fish", "expected": False},
        {"pattern": "aaaa", "s": "dog cat cat dog", "expected": False},
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        result = solver.wordPattern(sample["pattern"], sample["s"])
        print(f"Sample {i} result: {result}")
        print(f"Sample {i} expected: {sample['expected']}")
