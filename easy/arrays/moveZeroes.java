class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length <= 1) return;
        
        /**
         * Have two pointers - a read pointer and a write pointer.
         * The read pointer will look for non-zero elements and the write pointer
         * holds at zero elements until the read pointer locates a non-zero element.
         * When the read pointer finds a non-zero element and the write pointer is at
         * a zero element, the elements that the read and write pointer are pointing
         * to are swapped. This is done until the read pointer has exhausted the
         * array. The write pointer advances when a swap occurs or if it is not
         * pointing at a zero element.
         */
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
