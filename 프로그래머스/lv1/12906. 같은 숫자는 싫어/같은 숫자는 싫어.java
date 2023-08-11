import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int n : arr) {
            if (list.isEmpty() || list.get(list.size() - 1) != n) {
                list.add(n);
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}