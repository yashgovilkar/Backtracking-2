#Time Complexity :O(n*2^n)
#Space Complexity :O(n)
#Did this code successfully run on Leetcode : yes

class Solution:
    def __init__(self):
        self.result = list()
    
    def _helper(self, s, idx, path):
        if idx == len(s):
            self.result.append(path[:])
            return
        
        for i in range(idx, len(s)):
            cur = s[idx:i+1]
            
            if self.isPalindrome(cur):
                path.append(cur)
                self._helper(s,i+1,path)
                path.pop()
    
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def partition(self, s: str):
        self._helper(s, 0, [])
        return self.result