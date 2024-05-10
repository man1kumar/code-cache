#Number of divisors 
#https://www.geeksforgeeks.org/problems/number-of-divisors1631/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def count_divisors(self, N):
        count = 0
        # Iterate through each number from 1 to square root of N
        for i in range(1, int(N**0.5) + 1):
            # If i is a divisor of N and divisible by 3
            if N % i == 0:
                # If i is divisible by 3, increment count
                if i % 3 == 0:  count += 1
                # Check if the other divisor is distinct and divisible by 3
                if i != N // i and (N // i) % 3 == 0:  count += 1
        return count
       
#{ 
 # Driver Code Starts
#Initial Template for Python 3#Back-end complete function Template for Python 3#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.count_divisors(N))
# } Driver Code Ends