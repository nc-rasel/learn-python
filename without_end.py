# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
  n = len(str)

  if n >= 2:
    # str[1:]  means everything except first one
    # str[-1]  means everything except the last one
    return str[1:-1]
