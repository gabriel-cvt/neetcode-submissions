class Solution {

    static HashMap<Character, Integer> populatedMap(String word) {
        HashMap<Character, Integer> map = new HashMap<>();

        for (char c : word.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        return map;
    }

    static boolean calculateAnagram(HashMap<Character, Integer> first, HashMap<Character, Integer> second) {
        for (char c : second.keySet()) {
            if (!first.containsKey(c)) return false;
            if (!second.get(c).equals(first.get(c))) return false;
        }
        return true;
    }
    
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> mapS = populatedMap(s);
        HashMap<Character, Integer> mapT = populatedMap(t);

        if (mapS.size() <= mapT.size()) {
            return calculateAnagram(mapS, mapT);
        }
        return calculateAnagram(mapT, mapS);
        
    }
}
