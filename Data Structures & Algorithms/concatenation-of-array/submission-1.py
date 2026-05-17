class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # O(n^2) solution
        ans = []
        i = 0
        j = len(nums)
        for num in nums:
            ans.insert(i, num) # O(n)
            ans.insert(j, num) # O(n)
            i += 1 
            j += 1 
        return ans

        