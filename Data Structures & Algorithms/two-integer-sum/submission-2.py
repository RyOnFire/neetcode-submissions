class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums):
            for index2, j in enumerate(nums):
                if index != index2 and i + j == target:
                    return [index, index2]

             

        