class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        numlen = len(nums)
        for i in range(numlen):
            if i == 0:
                left[i]=1
            else:
                left[i] = left[i-1]*nums[i-1] 
        i = numlen - 1
        while i >=0:
            if i == numlen-1:
                right[i] = 1
            else: 
                right[i] = right[i+1]*nums[i+1]
            i=i-1
        answer = [1]*len(nums)
        for i in range(numlen):
            answer[i]= left[i]*right[i]


        return answer
        