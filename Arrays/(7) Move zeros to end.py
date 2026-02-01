############
#Brute
############
def moveToEnd(arr):
  n = len(arr)
  if n <= 1:
    return arr

  res = [0] * n
  idx = 0

  for i in range(n):
    if arr[i] != 0:
      res[idx] = arr[i]
      idx += 1

  return res

###########
#Optimal
###########
def moveToEnd(arr):
  if len(arr) <= 1:
    return arr
  i = 0
  for j in range(len(arr)):
    if arr[j] != 0:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  return arr
