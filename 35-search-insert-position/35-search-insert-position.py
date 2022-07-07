class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       for i in range(len(nums)):
            if nums[0]>target:
                return 0
            if nums[i]==target:
                #print('i=',i)
                return i
            if i==len(nums)-1:  
                return i+1 
            if nums[i]<target and nums[i+1]>target:
                #print(i)
                return i+1
              
                