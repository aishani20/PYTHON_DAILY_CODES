class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        is_positive = n > 0  
        if is_positive:
            is_log_integer = log(n, 4).is_integer() 
            return is_log_integer  
        else:
            return False