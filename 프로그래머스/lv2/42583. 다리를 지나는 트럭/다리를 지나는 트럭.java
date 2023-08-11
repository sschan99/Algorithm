class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int len = truck_weights.length;
        int head = 0, next = 1, time = 1;
        int weightSum = truck_weights[0];
        int[] locations = new int[len];
        
        while (head < len) {
            for (int i = head; i < next; i++) {
                locations[i] += 1;
            }
            if (locations[head] == bridge_length) {
                weightSum -= truck_weights[head++];
            }
            if (next < len && weightSum + truck_weights[next] <= weight) {
                weightSum += truck_weights[next++];
            }
            time++;
        }
        return time;
    }
}