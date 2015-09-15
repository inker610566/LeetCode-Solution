class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())
            return "";
        int length = strs.size();
        string answer = strs.at(0);
        for(int i=1; i<length; i++) {
            string cmp = strs.at(i);
            string tmp = answer;
            answer = "";
            int length1 = tmp.length();
            int length2 = cmp.length();
            int limit = (length1<length2)?length1:length2;
            for(int j=0; j<limit; j++) {
                if (tmp[j] != cmp[j]) {
                    break;
                }
                answer.push_back(tmp[j]);
            }
        }
        return answer;
    }
};