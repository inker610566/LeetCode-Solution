class Solution {
public:
    int reverse(int x) {
        bool isNeg = (x < 0);
        if(isNeg) x = -x;
        unsigned long ans = 0;
        while(x){
            ans = ans*10 + x%10;
            x /= 10;
        }
        if(ans > 2147483647)
            return 0;
        if(isNeg) ans = -ans;
        return ans;
    }
};