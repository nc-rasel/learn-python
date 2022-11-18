# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  s = len(str)
  first_char = str[:1]
  last_char = str[-1:]
  new_string = str[:]
  if s >= 2:
#   if s > 1:  also work
    return last_char + str[1:-1] + first_char
  else:
    return new_string
