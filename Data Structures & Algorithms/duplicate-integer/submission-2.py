class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        found = False
        for num in nums:
            if num in seen:
                seen[num] += 1 
                found = True
            else:
                seen[num] = 1 
        return found 
        


                


        