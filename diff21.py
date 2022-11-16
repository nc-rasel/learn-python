# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

# need to focus on logic how to calculate absolute difference
def diff21(n):
  '''
  difference = n - 21
  if difference < 0:
    absolute_difference = difference * -1
  else:
    absolute_difference = difference

  if n > 21:
    absolute_difference = absolute_difference * 2
  return absolute_difference
  '''
  # solve using builtin python function
  # abs is absolute difference

  absolute_difference = abs(n - 21)
  if n > 21:
    absolute_difference = absolute_difference * 2
  return absolute_difference