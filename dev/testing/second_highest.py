def second_highest(nums):
    nums = list(set(nums))
    nums.sort()
    print(nums[-2]) 


nums = [1, 2, 3, 4, 4, 5]
obj = second_highest(nums)