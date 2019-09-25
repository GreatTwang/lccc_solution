def joseph_problem(number_n, start_number_k, number_m):
    joseph_arr = []
    for i in range(1, number_n + 1):
        joseph_arr.append(i)
    # print(joseph_arr)
    start = start_number_k
    length = len(joseph_arr)
 
    for j in range(length - 1):
        start = (start + number_m) % len(joseph_arr)
        joseph_arr.pop(start)
    return joseph_arr[0]
class Solution:
    def josephus(self, n, k): 
        if (n == 1): 
            return 0
        else:      
          # The position returned by  
          # josephus(n - 1, k) is adjusted 
          # because the recursive call 
          # josephus(n - 1, k) considers 
          # the original position  
          # k%n + 1 as position 1  
            return (self.josephus(n - 1, k) + k) % n

