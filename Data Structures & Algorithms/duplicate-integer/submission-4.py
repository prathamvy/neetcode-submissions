class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        has_dup = False
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
            if freq[num] > 1:
                has_dup = True
                break
        return has_dup

        