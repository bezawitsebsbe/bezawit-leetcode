class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over each character in the string in reverse order
        for char in reversed(s):
            current_value = roman_to_int[char]
            
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update previous value
            prev_value = current_value
        
        return total 
        