class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        result = [1]*n
        #pre
        prev=1
        for i in range(n):
            result[i]*=prev
            prev*=nums[i]

        post=1
        for i in range(1, n+1):
            result[-i]*=post
            post*=nums[-i]

        return result

        