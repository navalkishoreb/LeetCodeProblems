class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        current = []
        def dfs(target, index):
            print(current)
            if target < 0:
                return 
            
            if target == 0:
                res.append(current.copy())
                return
            
            for i in range(index, len(candidates)):
                c = candidates[i]
                if i > index and c == candidates[i-1]:
                    continue
                current.append(c)
                dfs(target - c, i+1)
                current.pop()
        dfs(target,0)
        return res 
