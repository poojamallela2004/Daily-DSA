###########
#Brute
###########
def union(arr1, arr2):
  s = set()
  for x in arr1:
    s.add(x)
  for x in arr2:
    s.add(x)
  return list(s)


############
#Optimal
############
def union(arr1, arr2):
  i, j = 0, 0
  res = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      if not res or res[-1] != arr1[i]:
        res.append(arr1[i])
      i += 1
    elif arr2[j] < arr1[i]:
      if not res or res[-1] != arr2[j]:
        res.append(arr2[j])
      j += 1
    else:  # equal elements
      if not res or res[-1] != arr1[i]:
        res.append(arr1[i])
      i += 1
      j += 1
  while i < len(arr1):
    if res[-1] != arr1[i]:
      res.append(arr1[i])
    i += 1
  while j < len(arr2):
    if res[-1] != arr2[j]:
      res.append(arr2[j])
    j += 1
  return res
