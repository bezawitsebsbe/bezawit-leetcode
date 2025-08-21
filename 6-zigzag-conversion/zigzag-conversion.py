class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  # No conversion needed

        # Create a list to hold strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char  # Add the character to the current row
            # Change direction if we hit the top or bottom row
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            # Move to the next row
            current_row += 1 if going_down else -1

        # Join all rows to get the final result
        return ''.join(rows)
        