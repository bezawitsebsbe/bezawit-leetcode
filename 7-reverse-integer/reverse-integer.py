class Solution:
    def reverse(self, x: int) -> int:
        # Define the limits for a signed 32-bit integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Store the sign of x and work with its absolute value
        sign = -1 if x < 0 else 1
        x *= sign
        
        # Reverse the digits
        reversed_x = 0
        while x:
            digit = x % 10
            x //= 10
            
            # Check for overflow before actually adding the digit
            if (reversed_x > (INT_MAX - digit) // 10):
                return 0
            
            reversed_x = reversed_x * 10 + digit
        
        return sign * reversed_x
        