class MinStack {

    private List<Integer> stack;
    private List<Integer> minStack;

    public MinStack() {
        this.stack = new ArrayList<>();
        this.minStack = new ArrayList<>();
    }
    
    public void push(int val) {
        this.stack.add(val);

        if (this.minStack.isEmpty()) {
            this.minStack.add(val);
        } else {
            int currentMin = this.minStack.get(this.minStack.size() -1);
            if (currentMin >= val) {
                this.minStack.add(val);
            }
        }
    }
    
    public void pop() {
        if (this.stack.isEmpty()) return;
        int stackIdx = this.stack.size() -1;
        int minStackIdx = this.minStack.size() -1;
        int current = this.stack.get(stackIdx);
        if (current == this.minStack.get(minStackIdx)) {
            this.minStack.remove(minStackIdx);
        }
        this.stack.remove(stackIdx);
    }
    
    public int top() {
        return this.stack.get(this.stack.size() -1);
    }
    
    public int getMin() {
        return this.minStack.get(this.minStack.size() - 1);
    }
}
