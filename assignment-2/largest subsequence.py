def max_subsequence_sum(nums):
    max_sum = current_sum = nums[0]
for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum
  return max_sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subsequence_sum(nums)
print("Maximum subsequence sum is:", result)
