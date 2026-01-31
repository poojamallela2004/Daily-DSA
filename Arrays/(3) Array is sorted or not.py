#############
#Brute
#############
def sOrNot(arr):
  if len(arr) < 2:
    return True
  ver = arr[:]
  ver.sort()
  if ver == arr:
    return True
  else:
    return False

#############
#Optimal
#############
def sOrNot(arr):
  if len(arr) < 2:
    return True
  for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
      return False
  return True
