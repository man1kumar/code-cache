#The dice problem 
#https://www.geeksforgeeks.org/problems/the-dice-problem2316/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def oppositeFaceOfDice(self, N):
        """
        Finds the opposite face on a standard 6-sided die given a face number (N).
        Args:
            N: The face number on the die (1 to 6).
        Returns:
            The opposite face number (1 to 6).
        """
        
        # Calculate the opposite face using the property: sum of opposite faces is 7
        return 7-N

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends