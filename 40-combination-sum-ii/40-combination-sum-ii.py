class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       candidates.sort()  
       comp=[]
       def dmp(j,out,sum):
          if sum==target:
             if out not in comp:
               comp.append(out.copy())
               return
          if j>=len(candidates) or sum>target:
             return
          out.append(candidates[j])      
          dmp(j+1,out,sum+candidates[j])
          out.pop()
          while(j+1<len(candidates) and candidates[j]==candidates[j+1]):
            j+=1  
          dmp(j+1 ,out,sum)        
       dmp(0,[],0)
       return comp 