def list_counts_4(nums):
    count = 0
    for num in nums:
        if num==4:
            count = count+1
    return count    

print(list_counts_4([1,4,4,8,4]))
