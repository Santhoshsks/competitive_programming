def nextPermutation(nums):
    for i in range(len(nums)-1,-1,-1):
            if i == 0:
                nums.reverse()
                return
            else:
                if nums[i] > nums[i-1]:
                    for j in range(len(nums)-1,i-1,-1):
                        if nums[j]>nums[i-1]:
                            nums[i-1],nums[j]=nums[j],nums[i-1]
                            nums[i:len(nums) + 1] = sorted(nums[i:len(nums)+ 1])
                            return
                    
nums = [3,6,4,2,1]
nextPermutation(nums)
print(nums)