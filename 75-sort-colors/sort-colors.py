class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count1=0
        count2=0
        count3=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                count1+=1
            if nums[i]==1:
                count2+=1
            if nums[i]==2:
                count3+=1
        nums[0:count1]=[0]*count1
        nums[count1:count1+count2]=[1]*count2
        nums[count1+count2:count1+count2+count3]=[2]*count3
        return nums


        