class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums) #n=length of nums array
        if n==1:    #Base case if there is only one house
            return nums[0] #Returns the value of the money in the only house in the array
        if n==2:    #Base case if there are only two houses
            return max(nums[0], nums[1])   #Returns the max value between the money in the first and second house
    memoization={0:nums[0], 1:max(nums[0], nums[1])}  #First value=0, max money=nums[0], same value for index 1
    def helper(i):
        if i in memoization:    #If already ran function on the value of i
            return memoization[i]
        else:
            memoization[i]=max(nums[i]+helper(i-2), helper(i-1))    #Returns max value between 1.The money in the current house+the max value of money at the house 2 steps back or 2.The max amount of money at the house 1 step back
            return memoization[i]

#Credit to Greg Hogg
