#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    // Method Description:
    // This method returns the k most frequent elements from the given vector `nums`.
    // It uses an unordered_map to count the frequency of each element and then sorts 
    // these elements into a vector of vectors called `bucketcount`, where the index
    // represents the frequency. The elements are then collected from the buckets 
    // starting from the highest frequency to ensure the top k frequent elements are 
    // chosen efficiently.

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countmap;  // To store the frequency of each number
        vector<vector<int>> bucketcount(nums.size() + 1);  // Buckets for frequencies, indexed by frequency

        // Count the frequency of each number in the input vector
        for (auto& num : nums) {
            countmap[num]++;  // Increment the count for the number
        }

        // Place each number in the appropriate bucket based on its frequency
        for (auto& c : countmap) {
            bucketcount[c.second].push_back(c.first);  // c.second is the frequency, c.first is the number
        }

        vector<int> results;  // This will store the final results

        // Iterate from the highest possible frequency to the lowest
        for (int i = bucketcount.size() - 1; i >= 0 && results.size() < k; i--) {
            if (!bucketcount[i].empty()) {  // Check if the current bucket is not empty
                // Insert all numbers from this bucket into results
                results.insert(results.end(), bucketcount[i].begin(), bucketcount[i].end());
            }
        }

        // Return the vector containing the k most frequent elements
        return results;
    }
};
