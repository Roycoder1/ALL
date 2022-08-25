nums = [12, -7, 20, 1, 4, -10, -1]

# def subsetsum(nums,target):
#     for n in nums:
#         if (target-n) in nums:
#             return True
#         else:
#             return False

# print(subsetsum(nums, 1)) # False
# print(subsetsum(nums, 2)) # True: 12,  -10
# print(subsetsum(nums, 3)) # True: 4,  -1
# print(subsetsum(nums, 4)) # False

# second way:

def subsetsum1(nums):


    while len(nums)>0:
        r = nums[0]-1
        len(nums)-1
        
        print(r)#11
        if nums[0] == r:
            print(True) 
        else:
            print(False)
            
print(subsetsum1(nums))



