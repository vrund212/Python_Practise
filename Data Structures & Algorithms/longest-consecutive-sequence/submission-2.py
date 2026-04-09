class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        Length = 0

        for n in nums:
            if (n-1) not in numset:
                while(n+Length) in numset:
                    Length = Length + 1
                longest = max(Length,longest)
        return longest

        