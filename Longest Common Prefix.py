class Solution:
    #divide and conquer approach
    def longestCommonPrefix(self, strs: List[str]) -> str:
            return commonPrefix(strs, 0, len(strs) - 1)
        
def commonPrefix(str, s, e):

    if s == e:
        p = str[s]
        return p

    else:
        q = (e + s)//2
        lprefix = commonPrefix(str, s, q)
        rprefix = commonPrefix(str, q+1, e)
        cprefix = ""
        
        for index in range(min(len(lprefix), len(rprefix))):
            if lprefix[index] == rprefix[index]:
                cprefix += lprefix[index]
            else:
                break

        return cprefix
