# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def searchRange(self, nums: List[int], target: int) -> List[int]:

	left = self.binSearch(nums, target, True)
	right = self.binSearch(nums, target, False)
	return [left, right]

# leftBias = T/F, if false, res is rightBiased
def binSearch(self, nums, target, leftBias):
	l, r = 0, len(nums - 1)
	index = -1
	while l <= r:
		mid = (l+r)//2
		if target > nums[mid]:
			l = mid + 1
		elif target < nums[mid]:
			r = mid - 1
		else:
			index = mid
			if leftBias:
				r = mid - 1
			else:
				l = mid + 1
	return index