'''
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''

def first_last6(nums):
  
  '''
  # way - 1
  output = len(nums)
  
  if (nums[0] == 6 or nums[- 1] == 6):
    return True
  return False
  
  '''
  '''
  # way - 2
  get_first_6 = nums[0]
  get_last_6 = nums[-1]
  
  if get_first_6 == 6:
    return True
  elif get_last_6 == 6:
    return True
  else:
    return False
    
  
  first_last = nums[::len(nums)-1]
  if first_last == 6:
    return True
  else:
    return False
    
  '''
  
  first_last = nums[::len(nums)-1]
  
  if 6 in nums:
    return True
  else:
    return False
    
    
  