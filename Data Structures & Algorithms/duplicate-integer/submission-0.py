class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        n= len(nums)
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False       

