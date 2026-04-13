class Solution {
    HashSet<Integer> var = new HashSet<>();

    public boolean hasDuplicate(int[] nums) {
        
        for (int i = 0; i < nums.length; i++) {
            if (var.contains(nums[i])) return true;
            else var.add(nums[i]);
        }
        return false;
    }
}