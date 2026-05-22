class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramMap = defaultdict(list)

        for word in strs:
            sortWord = ''.join(sorted(word))
            anagramMap[sortWord].append(word)

        results = []
        for key in anagramMap.keys():
            results.append(anagramMap[key])
        
        return results



        