class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in number:
                return [number[difference], i]
            number[num] = i
