class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newarray = []
        for i in nums:
            new_val = i**2
            newarray.append(new_val)
        newarray.sort()
        return newarray

        