class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t) # This also works
        
        if len(s) != len(t):
            return False
        countS,countT = {},{}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for j in countS:
            if countS[j] != countT.get(j,0):
                return False
        return True

# make two dictionaries for each strings, store value as number of occurance with key as alphabelt , check value of both dictionaries for each all keys, use get(key,0) to avoid error if a key is not present in second dict 
