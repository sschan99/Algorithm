import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> result = new ArrayList<>();
        
        int now = 0;
        while (now < progresses.length) {
            for (int i = 0; i < progresses.length; i++) {
                progresses[i] += speeds[i];
            }
            
            if (progresses[now] >= 100) {
                int count = 0;
                for (int j = now; j < progresses.length; j++) {
                    if (progresses[j] < 100) break;
                    count++;
                }
                
                result.add(count);
                now += count;
            }
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}