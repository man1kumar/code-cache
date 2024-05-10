#Sum of digit is pallindrome or not 
#https://www.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def isDigitSumPalindrome(self, n):
        """
        Checks if the sum of digits of a number is a palindrome.
        Args:
            n: The integer to be checked.
        Returns:
            1 if the digit sum is a palindrome, 0 otherwise.
        """

        # Calculate the digit sum
        n = str(n) # Convert the number to a string
        digit_sum = sum(map(int,n))
        
        # Reverse the digit sum (using string conversion)
        reversed_sum = int(str(digit_sum)[::-1])

        # Check if the digit sum is a palindrome
        return 1 if digit_sum == reversed_sum else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends