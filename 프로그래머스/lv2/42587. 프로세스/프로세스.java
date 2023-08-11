class Solution {
    public int solution(int[] priorities, int location) {
        boolean[] done = new boolean[priorities.length];
        int next = 0;
        int maxPriority = 0;
        int order = 1;
        
        while (true) {
            int prev = next;
            for (int i = 0; i < priorities.length; i++) {
                int index = (prev + i) % priorities.length;
                
                if (done[index]) continue;
                
                if (maxPriority < priorities[index]) {
                    maxPriority = priorities[index];
                    next = index;
                }
            }
            
            if (next == location) return order;
            
            done[next] = true;
            maxPriority = 0;
            order++;
        }
    }
}