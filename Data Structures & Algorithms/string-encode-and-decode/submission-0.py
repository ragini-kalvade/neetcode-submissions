class Solution:

    def encode(self, strs: List[str]) -> str: 
        encode = []
        for string in strs:
            encode.append(str(len(string))+"#"+ string)
        
        encodedStr = ''.join(encode)
        return encodedStr

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        #iterate through the character to separate into words by identifiying the delimiter 
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            #i:j because word length can be multiple digits also
            word_len = int(s[i:j])

            word_start = j+1
            word_end = word_start + word_len 

            result.append(s[word_start:word_end])
            i = word_end
        
        return result