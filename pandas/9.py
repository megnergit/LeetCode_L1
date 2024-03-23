
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        rx = int(str(x)[::-1])
        if x-rx==0: 
            return True
        else:
            return False


x = 120024
z=Solution()
z.isPalindrome(x)

