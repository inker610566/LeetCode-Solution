class Solution {
public:
    int myAtoi(string str) {
        int ans = 0;
        int length = str.length();
        if(length == 0) return 0;
        
        int start = 0;
        for(start; str[start] == ' '; start++);
        
        int digit = 0;
        bool negative = false;
        if(isdigit(str[start])) {
            ans = (int)str[start]-48;
            digit++;
        } else {
            if(str[start] == '-') {
                negative = true;
            } else if(str[start] == '+'){
                negative = false;
            } else {
                return 0;
            }
        }
        
        for(int i=start+1; i<length && isdigit(str[i]); i++) {
            ans = ans*10 + (str[i]-'0');
            digit++;
        }
        if(negative)
            ans = -ans;
        if(!negative && (ans == -2147483648 || digit > 10))
            return 2147483647;
        else if(negative && (ans == 2147483647 || digit>10))
            return -2147483648;
            
        return ans;
    }
};