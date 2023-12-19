class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>s;
        vector<int> vect;
        for (int i=0;i<=nums.size();i++){
        
        if (s.find(target-nums[i])!=s.end())
        {
            vect.push_back(i);
            vect.push_back(s.at(target-nums[i]));
            return vect;
        }
        s[nums[i]]=i;
        }
        return vect;
    }
    
};