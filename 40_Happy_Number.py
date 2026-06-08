class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        
        while n != 1:
            if n in seen_numbers:
                return False
            seen_numbers.add(n)
            
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n //= 10
            n = sum_of_squares
            
        return True
