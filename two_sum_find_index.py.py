
# TWO SUM
# input =[2,7,11,15] target=9 
# o/p= indexes of elem whose sum is target => [0,1]
# class Solution(object):
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res=[]
    print(">>>",nums,target)
    t= target
    nums=[int(x) for x in nums]
    print(type(nums))
    # nums=int(nums)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
        	if nums[i] + nums[j] == t:
        		return [i,j]
        	else:
        		pass

nums=input("Enter List elem ").split(' ')
nums=list(nums)
target=int(input("Enter target number"))
two=twoSum(nums,target)
print("Output >>",two)