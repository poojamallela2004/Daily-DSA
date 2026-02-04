#########
#Brute
#########
def missing(arr):
  n = len(arr)
  for num in range(n + 1):
    if num not in arr:
      return num

##########
#Optimal
##########
def missing(arr):
  return len(arr)*(len(arr) + 1) // 2 - sum(arr)
