import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int s : scoville) heap.add(s);
        
        int count = 0;
        while (heap.peek() < K) {
            if (heap.size() == 1) return -1;
            
            heap.add(heap.poll() + heap.poll() * 2);
            count++;
        }
        return count;
    }
}