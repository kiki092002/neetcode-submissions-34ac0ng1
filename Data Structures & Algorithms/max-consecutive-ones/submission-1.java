class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int total_ones = 0;
        int max_consecutive_one = 0;
        for (int index = 0 ; index < nums.length; index++){
            if (nums[index] == 1){
                total_ones +=1;
            
            }
            else{
                total_ones =0;
            }
            max_consecutive_one = Math.max(max_consecutive_one , total_ones);
        }
        return max_consecutive_one;
    }
}