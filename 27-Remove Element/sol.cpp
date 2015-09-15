class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int countRes = count(nums.begin(), nums.end(), val);
        return nums.size() - countRes;
    }
};