class Solution:
    def sortColors(self, nums: List[int]) -> None:
        result=[]
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                    count+=1
        return result
                    
        
        """
        Do not return anything, modify nums in-place instead.
        """
