#########
# Brute
#########
def long(arr, k):
    n = len(arr)
    max_len = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len, j - i + 1)

    return max_len


###########
#Optimal
###########
def long(arr, k):
  max = 0
  prefix_sum = 0
  hm = {}
  for i in range(len(arr)):
    prefix_sum += arr[i]
    if prefix_sum == k:
      max = i + 1
    elif prefix_sum - k in hm:
      max = max(max, i - hm[prefix_sum - k])
    elif prefix_sum not in hm:
      hm[i] = prefix_sum
  return max
