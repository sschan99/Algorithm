import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int len = citations.length;
        Arrays.sort(citations);
        
        for (int i = 0; i < len; i++) {
            int index = len - 1 - i;
            if (citations[index] < i + 1) return i;
        }
        return len;
    }
}
