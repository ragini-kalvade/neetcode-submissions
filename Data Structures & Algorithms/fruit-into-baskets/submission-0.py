class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        type_fruit = {}
        max_len = 0
        for right in range(len(fruits)):
            type_fruit[fruits[right]] = type_fruit.get(fruits[right],0)+1

            while len(type_fruit)> 2:
                type_fruit[fruits[left]]= type_fruit.get(fruits[left],0)-1
                if type_fruit[fruits[left]] == 0:
                    del type_fruit[fruits[left]]
                left+=1
            max_len = max(max_len,right - left + 1)
        return max_len
