class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        h= set(nums)
        longest=0
        for n in h:
            if n-1 not in h:
                length=1
                next_n= n+1
                while next_n in h:
                    length+=1
                    next_n+=1
                longest = max(length, longest)
        return longest