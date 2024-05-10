#GCD of two numbers 
#https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def gcd(self, a: int, b: int) -> int:
        """
        Calculates the GCD of two positive integers using the Euclidean Algorithm.
        Args:
            a: The first positive integer.
            b: The second positive integer.
        Returns:
            The GCD of a and b.
        """
        
        # Implement the Euclidean Algorithm for GCD calculation
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a  # GCD is the value of a when b becomes 0
 
#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)

# } Driver Code Ends