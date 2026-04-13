class Solution {
    HashSet<Integer> var = new HashSet<>();

    public boolean hasDuplicate(int[] nums) {
        
        for (int n : nums) {
            if (var.contains(n)) return true;
            else var.add(n);
        }
        return false;
    }
}