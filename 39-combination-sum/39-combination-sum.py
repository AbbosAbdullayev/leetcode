class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
          comb=[]
          def dfs(i, out, sum):
            if sum==target:
               comb.append(out.copy())
               return
            if i>=len(candidates) or sum>target:
               return

            out.append(candidates[i])
            dfs(i, out, sum+candidates[i])
            out.pop()
            dfs(i+1, out, sum) 
          dfs(0, [], 0)
          return comb 
