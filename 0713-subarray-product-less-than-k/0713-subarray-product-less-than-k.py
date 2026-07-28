class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # a = [10, 5, 2, 6]
        # k = 100
        # n = len(a)
        # for i in range(n):
        #     prod = 1
        #     for j in range(i + 1, n + 1):
        #         prod *= a[j - 1]
        #         if prod < k:
        #             print(a[i:j])


        # n=len(nums)
        # count=0
        # for i in range(n):
        #     prod=1
        #     for j in range(i+1,n+1):
        #         prod*=nums[j-1]
        #         if prod<k:
        #             count+=1
        #         else:
        #             break
        # return count


        if k<=1:
            return 0
        l=0
        prod=1
        count=0
        for r in range(len(nums)):
            prod*=nums[r]
            while prod>=k:
                prod//=nums[l]
                l+=1
            count+=r-l+1
        return count
