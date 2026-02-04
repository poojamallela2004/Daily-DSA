#########
#Brute
#########
def twice(arr):
  for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
      if arr[i] == arr[j]:
        count += 1
    if count == 1:
      return arr[i]

#########
#Optimal
#########
def twice(arr):
  xor = 0
  for i in arr:
    xor = xor ^ i
  return xor
