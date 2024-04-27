class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>summap;
        int n=nums.size()
        for (int i=0;i<n;i++)
        {
            int value=target-nums[i];
            if (summap.find(value)!=summap.end())
            {   
                return {summap[value],i};
            }
            summap.insert({nums[i],i});

        }
        return {};

    }
};