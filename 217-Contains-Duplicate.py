class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            return True
   
# used set to get number of unique elements, checked length with length of list
