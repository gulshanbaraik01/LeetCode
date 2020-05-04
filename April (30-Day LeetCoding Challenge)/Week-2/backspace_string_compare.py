class Solution:
    def checkString(self, S):
        ans = []
        
        for i in S:
            if i != '#':
                ans.append(i)
            else:
                if len(ans):
                    ans.pop()
        
        return ''.join(ans)
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.checkString(S) == self.checkString(T)
        