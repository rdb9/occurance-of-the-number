#program to count occurance of number
def list_count_4(nums):   #function definition
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))    #function call
