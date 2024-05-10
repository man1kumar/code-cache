#Armstrong Numbers 
#https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def armstrongNumber (self, n):
        """
        Checks if a given number is an Armstrong number (sum of digit cubes equals the number itself).
        Args:
            n: The integer to be checked.
        Returns:
            "Yes" if it's an Armstrong number, otherwise "No".
        """
        # Convert the integer to a string to access digits
        num_str, sum_of_cubes = str(n), 0

        # Calculate the sum of cubes of digits
        for digit in num_str:  sum_of_cubes += int(digit) ** 3

        # Check if the sum equals the original number
        return "Yes" if sum_of_cubes == n else "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends