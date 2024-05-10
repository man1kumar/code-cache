#Odd or even 
#https://www.geeksforgeeks.org/problems/odd-or-even3618/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def oddEven (ob,N):
        """
        Checks if a number is odd or even and returns a string indicating the result.
        Args:
            N: The integer to be checked.
        Returns:
            "odd" if N is odd, "even" otherwise.
        """
        
        # Use modulo operator (%) to check for divisibility by 2
        return "odd" if N%2==1 else "even" 

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.oddEven(N))
# } Driver Code Ends