class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;
        Stack<Character> stack =  new Stack<>();
    
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '}') {
                if (stack.empty() || stack.pop() != '{') return false;
            }
            else if (s.charAt(i) == ')') {
                if (stack.empty() || stack.pop() != '(') return false;
            }
            else if (s.charAt(i) == ']') {
                if (stack.empty() || stack.pop() != '[') return false;
            }
            else {
                stack.push(s.charAt(i));
            }
        }
        if (!stack.empty()) return false;
        return true;
    }
}
