import re
LARGE_UNITS = list(reversed(["", "Thousand", "Million", "Billion", "Trillion"]))
Dx = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
D1x = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
Dx0 = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        result = []
        s = str(num)
        ug = re.findall("...", str(num)[len(s)%3:])
        if len(s)%3: ug = [s[:len(s)%3]] + ug
        for unit, ug in zip(LARGE_UNITS[-len(ug):], ug):
            ugv = int(ug)
            if ugv == 0: continue
            # hundred
            if ugv >= 100:
                result += [Dx[ugv/100], "Hundred"]
                ugv %= 100
            # below
            if ugv >= 20:
                result += [Dx0[ugv/10], Dx[ugv%10]]
            elif ugv >= 10:
                result += [D1x[ugv-10]]
            else:
                result += [Dx[ugv]]
            result += [unit]
            
        return " ".join(filter(lambda x: x, result))
 
if __name__ == "__main__":
    print Solution().numberToWords("1012")
