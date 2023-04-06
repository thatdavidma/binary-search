# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

def mySqrt(self, x: int) -> int:
    if x == 0:
        return 0
    first, last = 1, x
    while first <= last:
        mid = first + (last - first) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            last = mid - 1
        else:
            first = mid + 1
    return last