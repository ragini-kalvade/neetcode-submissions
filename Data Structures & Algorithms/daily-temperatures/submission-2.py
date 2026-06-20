class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #store temps in stack. if current temp is greater than last temp in stack 
        #add to results with index difference

        results = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return results
        