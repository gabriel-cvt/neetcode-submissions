class Solution {

    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int result = 0;

        for (int n : nums) {
            set.add(n);
        }

        int length = 1;
        int current = 0;
        for (int n : set) {
            if (!set.contains(n -1)) {
                current = n;
                length = 1;
                while(set.contains(current + 1)) {
                    current++;
                    length++;
                }
                result = Math.max(result, length);
            }
        }
        return result;
    }
}
