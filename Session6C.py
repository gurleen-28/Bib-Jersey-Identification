def square_of_numbers(nums):
    print("1.NUMBER IS:",nums)
    
    for idx in range(0,len(nums)):
      nums[idx]*=nums[idx]
    
    
    print("2.NUMBER IS:",nums)
    return
    
numbers=[10,20,30,40,50]
print("A.NUMBER IS:",numbers)
square_of_numbers(numbers)
print("B.NUMBER IS:",numbers)