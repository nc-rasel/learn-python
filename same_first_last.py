"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""


def same_first_last(nums):
    x = len(nums)
    print(x)

    if x >= 1:
        if nums[0] == nums[-1]:
            return True
        else:
            return True
    else:
        return False

    """
	if x >= 1 and (nums[0] == nums[-1]):
    return True
  else:
    return False
	"""


same_first_last([1, 2, 3, 1])
