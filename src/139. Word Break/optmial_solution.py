class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        maxLen = max(len(w) for w in wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for l in range(1, min(i, maxLen) + 1):
                if dp[i - l] and s[i - l:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
