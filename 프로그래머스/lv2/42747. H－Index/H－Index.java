import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int len = citations.length;
        
        Integer[] copy = new Integer[len];
        for (int i = 0; i < len; i++) {
            copy[i] = citations[i];
        }
        
        Arrays.sort(copy, (x, y) -> y - x);
        
        for (int i = 0; i < len; i++) {
            if (copy[i] < i + 1) return i;
        }
        return len;
    }
}