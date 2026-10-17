class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums
        for idx, i in enumerate(nums):
            for idy, x in enumerate(nums2):
                if x + i == target and idx != idy:
                    if idx <= idy:
                        return [idx,idy]
                    else:
                        return [idy,idx]
                else:
                    continue
        return False