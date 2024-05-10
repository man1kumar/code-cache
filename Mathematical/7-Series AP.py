#Series AP 
#https://www.geeksforgeeks.org/problems/series-ap5310/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        """
        Calculates the nth term of an Arithmetic Series (AP) given the first two terms.
        Args:
            a1: The first term of the AP.
            a2: The second term of the AP.
            n: The term number to be calculated (positive integer).
        Returns:
            The nth term of the AP.
        """

        # Formula for nth term of AP: a_n = a1 + d(n - 1)
        # where d is the common difference (a2 - a1)
        return a1 + (a2 - a1) * (n - 1) 

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a1 = int(input())
        
        a2 = int(input())
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthTermOfAP(a1, a2, n)
        
        print(res)
# } Driver Code Ends