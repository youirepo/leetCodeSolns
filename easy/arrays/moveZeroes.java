class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length <= 1) return;
        
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] == 0) continue;
            
            if (nums[i] == 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
            i++;
        }
    }
}
