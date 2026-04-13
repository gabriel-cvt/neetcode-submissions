
class Solution {
    HashMap<Character, Integer> map = new HashMap<>();

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        for (int i = 0; i < s.length(); i++) {
            map.merge(s.charAt(i), 1, Integer::sum);
            map.merge(t.charAt(i), -1, Integer::sum);
        }

        for (Integer i : map.values()) {
            if (i != 0)
                return false;
        }
        return true;
    }
}
