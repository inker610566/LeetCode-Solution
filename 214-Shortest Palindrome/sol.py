def KMP(s, p):
    '''
        :Args:
            - s : string to be matched
            - p : pattern
        :Return:
            - a list
    '''
    def build_failure(s):
        f, j = [-1], -1
        for i, c in (lambda e: (next(e), e)[1])(enumerate(s)):
            while j != -1 and s[j+1] != c:
                j = f[j]
            if s[j+1] == c: j += 1
            f += [j]
        return f
    p = p + '$' # guard char
    f = build_failure(p)
    # match
    j = -1
    ret = []
    for i, c in enumerate(s):
        while j != -1 and p[j+1] != c:
            j = f[j]
        if p[j+1] == c: j += 1
        ret += [j+1]

    return ret

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1: return s
        m = KMP(s[-1::-1], s)[-1::-1]
        ans = 0
        for i in range(len(m)):
            # i not as center: s[i::-1] match s[i+1:x]
            if i+1 < len(m) and m[i+1] >= i+1:
                ans = max(ans, i+i+2)
            # i as center: s[i-1::-1] match s[i+1:x]
            if i+1 < len(m) and m[i+1] >= i:
                ans = max(ans, i*2+1)

        return s[-1:-(len(s)-ans+1):-1]+s

if __name__ == '__main__':
    print Solution().shortestPalindrome('a')
