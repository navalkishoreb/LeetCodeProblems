class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        def dfs(target, index):
            if target < 0:
                return 
            
            if target == 0:
                res.append(current.copy())
                return
            
            for i in range(index, len(candidates)):
                c = candidates[i]
                current.append(c)
                dfs(target - c, i)
                current.pop()
        dfs(target,0)
        return res 
