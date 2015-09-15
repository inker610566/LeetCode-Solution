class Solution {
public:
    bool isValid(string s) {
        int length = s.length();
        string stack = "";
        for(int i=0; i<length; i++) {
            switch(s[i]) {
                case '(':
                    stack.push_back('(');
                    break;
                case '[':
                    stack.push_back('[');
                    break;
                case '{':
                    stack.push_back('{');
                    break;
                case ')':
                    if(stack.back() == '('){
                        stack.pop_back();
                    } else {
                        return false;
                    }
                    break;
                case ']':
                    if(stack.back() == '['){
                        stack.pop_back();
                    } else {
                        return false;
                    }
                    break;
                case '}':
                    if(stack.back() == '{'){
                        stack.pop_back();
                    } else {
                        return false;
                    }
                    break;
            }
        }
        return stack.empty();
    }
};