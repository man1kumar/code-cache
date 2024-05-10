#Addition of two numbers 
#https://www.geeksforgeeks.org/problems/addition-of-two-numbers0812/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def addition (ob,A,B):
        """
        Calculates the sum of two integers.
        Args:
            A: The first integer.
            B: The second integer.
        Returns:
            The sum of A and B.
        """

        return A + B   # Simply add the two numbers

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.addition(A,B))
# } Driver Code Ends