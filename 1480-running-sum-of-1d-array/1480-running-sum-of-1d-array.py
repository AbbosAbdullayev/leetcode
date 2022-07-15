class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=[]
        for i in range(1,len(nums)+1):
            m=0
            for j in range(i):
               m+=nums[j]
            sums.append(m)
        return sums       