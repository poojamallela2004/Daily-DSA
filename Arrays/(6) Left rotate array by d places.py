#############
#Brute
#############
def dPlaces(arr, d):
  if len(arr) <= 1:
    return arr
  d =d%len(arr)
  for _ in range(d):
    temp = arr[0]
    for i in range(1, len(arr)):
      arr[i-1] = arr[i] 
    arr[-1] = temp
  return arr

##############
#Optimal
##############
def dPlaces(arr, d):
  if len(arr) <= 1:
    return arr
  d = d%len(arr)
  rev(arr, 0, d-1)
  rev(arr, d, len(arr) -1)
  rev(arr, 0, len(arr) -1)
  return arr

def rev(arr, i, j):
  while(i<j):
    arr[i] ,arr[j] = arr[j], arr[i]
    i+=1
    j-=1
  
