class Solution {
    public record Pair(int tmp, int index) {}

    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        Stack<Pair> stack = new Stack<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.empty() && stack.peek().tmp() < temperatures[i]) {
                Pair top = stack.peek();
                result[top.index] = i - top.index();
                stack.pop();
            }
            Pair newP = new Pair(temperatures[i], i);
            stack.push(newP);
        }
        return result;
    }
}
