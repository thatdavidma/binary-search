# 744. Find Smallest Letter Greater Than Target

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    # if the number is out of bound
    if target >= letters[-1] or target < letters[0]:
        return letters[0]
    l = 0
    r = len(letters)-1
    while l <= r:
        mid = (r+l)//2
        if  target >= letters[mid]: # in binary search this would be only greater than
            l = mid + 1
        if target < letters[mid]:
            r = mid - 1
    return letters[l]