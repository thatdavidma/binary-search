# 1608. Special Array With X Elements Greater Than or Equal X

# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

def specialArray(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    if n<=nums[0]:
        return n
    #binary search
    start,end = 0,n
    while(start<=end):
        mid = (start+end)//2
        #index of middle element
        count = 0
        for i in range(0,n):
            if nums[i]>=mid:
                count = n-i
                break
        if count==mid:
            return count
        elif count<mid:
            end = mid-1
        else:
            start=mid+1            
    return -1