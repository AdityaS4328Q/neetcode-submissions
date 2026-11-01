class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            n=len(i)
            encoded_str+=str(n)+"#"+i
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_str=[]
        
        i=0
        while i < len(s):
            x= s.find('#', i)
            length= int(s[i:x])
            decoded_str.append(s[x+1: x+1+ length])
            i=1+x+length


        return decoded_str