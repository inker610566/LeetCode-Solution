class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_end_here = nums[0];
        int max_so_far = nums[0];
        int length = nums.size();
        for(int i=1; i<length; i++) {
            max_end_here = (nums[i] > nums[i]+max_end_here)?nums[i]:nums[i]+max_end_here;
            max_so_far = (max_so_far > max_end_here)?max_so_far:max_end_here;
        }
        return max_so_far;
    }
};
