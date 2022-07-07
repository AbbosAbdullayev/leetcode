class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
           end=-1
           start=-1
           for i in range(len(nums)):
             if nums[i]==target:
                start=i
                for j in range(len(nums)-1,start,-1):
                    if nums[j]==target:
                        end=j
                        break
                break  
           if end==-1 and start!=-1:
             end=start

           return [start,end] 