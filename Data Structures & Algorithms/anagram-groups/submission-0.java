class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] array = str.toCharArray();
            Arrays.sort(array);
            String sort = new String(array);

            if (map.containsKey(sort)) {
                map.get(sort).add(str);
            } else {
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(sort, list);
            }
        }
        return new ArrayList<>(map.values());
    }
}
