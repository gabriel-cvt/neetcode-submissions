class Solution {
    
    public boolean isPalindrome(String s) {
        StringBuilder builder = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) builder.append(c);
        }

        String lower = builder.toString().toLowerCase();
        
        int start = 0;
        int end = lower.length() -1;
        while (start < end) {
            if (lower.charAt(start++) != lower.charAt(end--))
                return false;
        }
        return true;
    }
}
