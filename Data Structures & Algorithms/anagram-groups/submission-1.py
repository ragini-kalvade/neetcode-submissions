class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            anagram_dict.setdefault(sorted_str,[]).append(string)
        
        results = list(anagram_dict.values())
        
        return results