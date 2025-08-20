class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store characters in the current window
        left = 0  # Left pointer of the window
        max_length = 0  # Maximum length of substring found

        for right in range(len(s)):
            # If the character is already in the set, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the leftmost character
                left += 1  # Move the left pointer to the right

            char_set.add(s[right])  # Add the current character to the set
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
        