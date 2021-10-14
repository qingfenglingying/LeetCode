#题目
'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
'''
#题解
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    tmp = nums[0]
    idx = 0
    for c in nums[1:]:
        if c != tmp:
            tmp = c
            idx += 1
            continue
        else:
            nums.pop(idx)
    return len(nums)
