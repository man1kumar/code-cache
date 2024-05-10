#Greatest of three numbers 
#https://www.geeksforgeeks.org/problems/greatest-of-three-numbers2520/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def greatestOfThree(self,A,B,C):
        """
        Finds the greatest of three numbers using the built-in `max` function.
        Args:
            A (int): The first number.
            B (int): The second number.
            C (int): The third number.
        Returns:
            int: The greatest of the three numbers.
        """

        # Use the built-in max function to find the largest number
        return max(A, B, C) 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
# } Driver Code Ends