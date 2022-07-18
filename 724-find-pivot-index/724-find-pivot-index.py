class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
            P=sum(nums)
            if P-nums[0]==0:
                return 0
            for i in range(len(nums)):
                left=sum(nums[:i])
                right=P-left-nums[i]
                if left==right:
                    return i
            if P==nums[-1]:
                return 0
            return -1   