class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for sym in s:
            if sym in {'(','{','['}:
                ans.append(sym)
            elif sym in {')',']','}'}:
                if not ans:
                    return False
                elif sym == ')' and ans[-1] == '(':
                    ans.pop()
                elif sym == ']' and ans[-1] == '[':
                    ans.pop()
                elif sym == '}' and ans[-1] == '{':
                    ans.pop()
                else :
                    return False
        
        return  not ans
                


            