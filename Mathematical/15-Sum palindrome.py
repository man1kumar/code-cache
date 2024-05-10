#Sum palindrome 
#https://www.geeksforgeeks.org/problems/sum-palindrome3857/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def isSumPalindrome (self, n):
        """
        Checks if a number becomes a palindrome after a limited number of additions of its reverse.
        Args:
            n (int): The integer to check.
        Returns:
            int: The number itself if it becomes a palindrome within 6 iterations, otherwise -1.
        """

        # Loop for a maximum of 6 iterations
        for _ in range(6):
            # Check if the number is already a palindrome
            if str(n) == str(n)[::-1]:  return n

            # Add the reverse of the number to itself
            reverse = int(str(n)[::-1])
            n += reverse

        # If not a palindrome within 6 iterations, return -1
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends