import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int[] command : commands) {
            int i = command[0], j = command[1], k = command[2];
            
            int[] subset = Arrays.copyOfRange(array, i - 1, j);
            Arrays.sort(subset);
            result.add(subset[k - 1]);
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}