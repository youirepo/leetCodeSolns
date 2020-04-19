class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Have two pointers: fill and check
        // The check pointer iterates through array (i.e. moving pointer) starting from index = 1
        // Fill starts from beginning and only proceeds to next element when
        // check pointer finds an element that is not equal to where fill is currently pointing to.
        // Increment the fill pointer and "fill" it with value pointed to by check.
        // Do this until check iterates through the entire array
        // The length of new array is fill index + 1 (because array indices are zero based)
        
        if (nums.empty()) return 0;

        int fill = 0;
        for (int check = 1; check < nums.size(); check++)
        {
            if (nums[check] == nums[fill]) continue;
            else
            {
                ++fill;
                nums[fill] = nums[check];
            }
        }
        return ++fill;
    }
};
