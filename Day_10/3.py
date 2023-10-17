class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            # elif start==end:
            #     return start
            elif nums[mid]>target:
                start = mid+1
            elif nums[mid]<target:
                end = mid-1
        return -1
obj = Solution()
print(obj.searchInsert([1,3,5,6],5))