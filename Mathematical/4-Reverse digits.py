#Reverse digits 
#https://www.geeksforgeeks.org/problems/reverse-digit0316/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def reverse_digit(self, n: int) -> int:
        """
        Reverses the digits of an integer, ignoring leading zeroes.
        Args:
            n: The integer to be reversed.
        Returns:
            The reversed integer without leading zeroes, or 0 if the input is 0.
        """

        # Use string slicing and conversion to reverse and remove leading zeroes
        return int(str(n)[::-1])  
    
        # str(n) converts n to a string.
        # [::-1] reverses the string (slicing).
        # int() converts the reversed string back to an integer.
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends                                    