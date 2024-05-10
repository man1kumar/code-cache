#Simple Interest 
#https://www.geeksforgeeks.org/problems/simple-interest3457/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def simpleInterest(self,A,B,C):
        """
        Calculates the simple interest based on principal, rate, and time.
        Args:
            P (int): The principal amount.
            R (int): The rate of interest per annum (as a percentage).
            T (int): The time period in years.
        Returns:
            float: The simple interest.
        """
        # Simple Interest formula: SI = (P * R * T) / 100
        return A*B*C/100

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
# } Driver Code Ends