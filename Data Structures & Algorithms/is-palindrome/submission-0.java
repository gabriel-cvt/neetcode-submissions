class Solution {
    
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() -1;
        s = s.strip();

        while (start < end) {
            
            while (start < end && !Character.isLetterOrDigit(s.charAt(start))) {
                start++;
            }

            while (start < end && !Character.isLetterOrDigit(s.charAt(end))) {
                end--;
            }

            if (Character.toUpperCase(s.charAt(start)) != Character.toUpperCase(s.charAt(end))) {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }
}
