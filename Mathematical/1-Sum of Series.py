#Question - Sum of series 
#https://www.geeksforgeeks.org/problems/sum-of-series2811/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution:
    def seriesSum(self, n: int) -> int:
        """
        Calculates the sum of the series 1 + 2 + 3 + ... + n.
        Args:
            n: The upper limit of the series (inclusive).
        Returns:
            The sum of the series.
        """
        # Use the formula for sum of an arithmetic series: n * (n + 1) // 2
        # Explanation:
        # - This formula works because it takes the average of the first and last term
        #   in the series and multiplies it by the number of terms (n).
        # - // is the integer division operator, discarding any remainder.
        return n*(n+1)//2
#{
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
# } Driver Code Ends
