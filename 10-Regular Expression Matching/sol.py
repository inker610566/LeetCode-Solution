class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[loc_s][loc_p] = true|false
        # preprocess pattern
        pattern = []
        for i, c in enumerate(p):
            if c == '*':
                assert pattern and len(pattern[-1]) == 1
                pattern[-1] = pattern[-1]+'*'
            else:
                pattern += [c]
        n_s, n_p = len(s), len(pattern)
        dp = [ [False]*(n_p) for _ in range(n_s+2)]
        self.ans = False
        def update(floc_s, floc_p):
            #print (floc_s, floc_p)
            if floc_p >= n_p:
                if floc_s == n_s and floc_p == n_p:
                    self.ans = True
                return
            dp[floc_s][floc_p] = True
        s = s + '$' # dummy
        update(0,0)
        for i, cs in enumerate(s):
            for j, cp in enumerate(pattern):
                if dp[i][j]:
                    if len(cp) == 2:
                        if cp == '.*':
                            update(i, j+1) # skip
                            update(i+1, j)
                        else:
                            update(i, j+1) # skip
                            if cp[0] == cs:
                                update(i+1, j)
                    else:
                        if cp == '.' or cs == cp:
                            update(i+1, j+1)
        return self.ans

if __name__ == '__main__':
    print Solution().isMatch('aa', '.*')
