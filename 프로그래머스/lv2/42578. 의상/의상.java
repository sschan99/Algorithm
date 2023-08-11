import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> counter = new HashMap<>();
        
        for (String[] elem : clothes) {
            String kind = elem[1];
            Integer prev = counter.get(kind);
            counter.put(kind, prev == null ? 1 : prev + 1);
        }
        
        int result = 1;
        for (String key : counter.keySet()) {
            result *= counter.get(key) + 1;
        }
        return result - 1;
    }
}