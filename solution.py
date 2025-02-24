class Solution:
    def rotate(self, a, k):
        n = len(a)
        k = k % n  
        b = []
        
        for i in range(k):
            b.append(a[n - 1 - i])
        
        for j in range(n - k - 1, -1, -1):
            a[j + k] = a[j]
        
        for i in range(k):
            a[i] = b[k - 1 - i]
