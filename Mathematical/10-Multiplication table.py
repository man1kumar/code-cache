#Multiplication table 
#https://www.geeksforgeeks.org/problems/print-table0303/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def getTable(self,N):
        """
        Generates the multiplication table of a given number (N) and returns it as a list.
        Args:
            N: The number for which the multiplication table is to be generated.
        Returns:
            A list containing the multiplication table of N (1 x N to 10 x N).
        """

        # Use list comprehension for concise table generation
        return  [N*i for i in range(1,11)] 
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends