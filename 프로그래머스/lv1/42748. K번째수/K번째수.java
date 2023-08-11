import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> result = new ArrayList<>();
        for (int[] command : commands) {
            int i = command[0], j = command[1], k = command[2];
            int len = j - i + 1;
            
            int[] subset = new int[len];
            for (int l = 0; l < len; l++) {
                subset[l] = array[i - 1 + l];
            }
            Arrays.sort(subset);
            result.add(subset[k - 1]);
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}