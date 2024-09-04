class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        conj = set()
        for num in nums:
            if (num in conj):
                return True
            conj.add(num)
        return False