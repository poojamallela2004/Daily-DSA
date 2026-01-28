###############
#Brute
###############
def largest(arr):
  if not arr:
    return -1
  arr.sort()
  return arr[-1]

###############
#Optimal
###############
def largest(arr):
  if not arr:
    return -1
  largest = -1
  for i in range(len(arr)):
    largest = max(arr[i], largest)
  return largest
