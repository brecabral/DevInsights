class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            aux = nums.copy()
            del aux[i]
            if (num in aux):
                continue
            return num


lista = [1, 0, 1]
a = Solution()
print(a.singleNumber(lista))



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        v = 0
        for n in nums:
            v ^= n
        return v