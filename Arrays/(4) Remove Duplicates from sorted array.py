############
#Brute
############
def Remove(arr):
  res = []
  for i in range(len(arr)):
    if arr[i] not in res:
      res.append(arr[i])
  return res

############
#Optimal
############
def Remove(arr):
  i = 0
  for j in range(1,len(arr)):
    if arr[j] != arr[i]:
      i += 1
      arr[i] = arr[j]
  return i+1
