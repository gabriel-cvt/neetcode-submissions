class Solution {
    
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> count = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) +1);
            count.put(t.charAt(i), count.getOrDefault(t.charAt(i), 0) -1);
        }

        return (count.values().stream().allMatch(v -> v == 0));
    }
}
