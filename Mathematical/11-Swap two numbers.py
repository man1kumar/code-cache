#Swap two numbers 
#https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def get(self, a, b):
        """
        Swaps two numbers (a and b) and returns them in a list in the reversed order (b, a).

        Args:
            a: The first integer.
            b: The second integer.

        Returns:
            A list containing the swapped numbers (b, a).
        """
        return [b, a] 

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a,b = map(int,input().strip().split())
		ob = Solution()
		ans=ob.get(a,b)
		print(str(ans[0])+" "+str(ans[1]))
# } Driver Code Ends