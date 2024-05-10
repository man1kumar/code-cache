#Find the median 
#https://www.geeksforgeeks.org/problems/find-the-median0527/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions

class Solution :
    def find_median(self, v):
      n = len(v)   #Finding List Length
      v.sort()    #Sorting the List
      return (v[(n-1)//2] + v[(n-1)//2 + ((n-1)%2)]) // 2
    
      #(n-1)//2: Calculates the middle element's index (or first middle element for even lists).
      #v[(n-1)//2]: Accesses the middle element (or first middle element).
      #((n-1)%2) checks if n is even (0 for even). If even, adds 1 to access the second middle element (v[(n-1)//2 + 1]).
      #Averages middle elements (even lists) or returns the single middle element (odd lists) using integer division (// 2)

#{
#Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
  T=int(input())
  for i in range(T):
    n = int(input())
    v = list(map(int,input().split()))
    ob = Solution();
    ans = ob.find_median(v)
    print(ans)

# } Driver Code Ends

