class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t: return ""
        def ctoi(c):
            xx = ord(c)
            if 0 <= xx < 256:
                return xx
            else:
                return -1
        t_cnt, s_cnt = [0]*(256), [0]*(256)
        t_n, s_n = len(t), len(s)
        for c in t:
            assert ctoi(c) != -1
            t_cnt[ctoi(c)] += 1
        ans_j, ans_i, ans = -1, -1, len(s) + 1
        j, good_num = 0, 0
        for i, c in enumerate(s):
            cc = ctoi(c)
            if cc != -1:
                # push i
                if s_cnt[cc] < t_cnt[cc]:
                    good_num += 1
                s_cnt[cc] += 1
            # try pop j
            while j < len(s) and (ctoi(s[j]) == -1 or s_cnt[ctoi(s[j])] > t_cnt[ctoi(s[j])]):
                if ctoi(s[j]) != -1:
                    s_cnt[ctoi(s[j])] -= 1
                j += 1
            # try compare ans
            if good_num == t_n and i-j+1 < ans:
                ans_i, ans_j, ans = i, j, i-j+1
        return "" if ans_j == -1 else s[ans_j: ans_i+1]

if __name__ == '__main__':
    print Solution().minWindow("aADOBECODEBANC", "bABC")
