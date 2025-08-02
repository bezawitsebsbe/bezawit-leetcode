class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
    # Sort the array
        strs.sort()
    
    # Take the first and last strings after sorting
        first = strs[0]
        last = strs[-1]
    
    # Find the common prefix between the first and last
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
    
        return first[:i]
       
        