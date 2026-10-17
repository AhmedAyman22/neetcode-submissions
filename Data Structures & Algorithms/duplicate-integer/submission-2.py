class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            print(f'{nums} == {set(nums)}')
            return False
        else:
            print(f'{nums} != {set(nums)}')
            return True
        # seen = []
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.append(i)
        # return False