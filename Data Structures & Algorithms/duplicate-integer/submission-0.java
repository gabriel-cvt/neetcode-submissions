class Solution {
    HashSet<Integer> set = new HashSet<Integer>();

    public boolean hasDuplicate(int[] nums) {
        for (int n : nums) {
            if (set.contains(n)) return true;
            else set.add(n);
        }
        return false;
    }
}