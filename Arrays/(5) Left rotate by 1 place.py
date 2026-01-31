#############
#Brute
#############
def rotateBy1(arr):
  temp = arr[0]
  for i in range(1,len(arr)):
    arr[i-1] = arr[i]
  arr[-1] = temp
  return arr

#############
#Optimal
#############
def rotateBy1(arr):
  if len(arr) == 0:
    return arr
  return arr[1:] + [arr[0]]
