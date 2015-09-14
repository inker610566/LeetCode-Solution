class Solution {
    
struct sort_pred {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.second < right.second;
    }
};

public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer(2);
        vector< pair<int, int> > list;
        for(int i=0; i<nums.size(); i++) {
            list.push_back(make_pair(i+1, nums[i]));
        }
        
        sort(list.begin(), list.end(), sort_pred());
        
        for(int i=0; i<list.size(); i++) {
            for(int j=i+1; j<list.size(); j++) {
                int sumup = list[i].second + list[j].second;
                if( sumup == target) {
                    answer[0] = (list[i].first < list[j].first)?list[i].first:list[j].first;
                    answer[1] = list[i].first + list[j].first - answer[0];
                    return answer;
                } else if(sumup > target) {
                    break;
                }
            }
        }
    }
};