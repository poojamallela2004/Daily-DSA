############
#Brute
############
def maxOnes(arr):
  n = len(arr)
  maxi = 0
  for i in range(n):
      count = 0
      for j in range(i, n):
          if arr[j] == 1:
              count += 1
              maxi = max(maxi, count)
          else:
              break
  return maxi


############
#Optimal 
############
def maxOnes(arr):
  if len(arr) < 2:
    return len(arr)
  count = 0
  max = 0
  for i in range(len(arr)):
    if arr[i] == 1:
      count += 1
      max = max(max, count)
    else:
      count = 0
  return max
