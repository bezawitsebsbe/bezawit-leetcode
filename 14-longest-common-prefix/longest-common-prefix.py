class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of the string
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Shorten the prefix
                if not prefix:  # If there's no common prefix
                    return ""

        return prefix
        