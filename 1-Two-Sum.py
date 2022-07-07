class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[n] = i
            
        # loop through the list, check the diff( target-number) and check if diff exist in the hashmap ... if no create a kep:value with number:index
        ####################################
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j] 
        # for loop through each elements twice and check if they adds up to target, start second loop from next element of first loop to avoid checking more than once for same pair
