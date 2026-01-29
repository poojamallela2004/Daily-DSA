#############
#Brute
#############
def sLargest(arr):
  if len(arr) < 2:
    return -1
  arr.sort()
  for i in range(len(arr)-2,-1,-1):
    if arr[i] != arr[i+1]:
      return arr[i]
  return -1

#############
#Optimal
#############
def sLargest(arr):
  if len(arr) < 2:
    return -1
  large = float("-inf")
  slarge = float("-inf")
  for i in range(1,len(arr)):
    if arr[i] > large:
      slarge = large
      large = arr[i]
    elif arr[i] != large and arr[i] > slarge:
      slarge = arr[i]
  if slarge == float("-inf"):
    return -1
  else:
    return slarge
