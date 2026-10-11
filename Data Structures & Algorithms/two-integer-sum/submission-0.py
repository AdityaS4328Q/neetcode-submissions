class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,v in enumerate(nums):
            t=target-v
            if v in seen:
                return [seen[v],i]
            else:
                seen[t]=i