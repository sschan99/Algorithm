import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> counter = new HashMap<>();
        for (String name : participant) {
            Integer prev = counter.get(name);
            counter.put(name, prev == null ? 1 : prev + 1);
        }
        for (String name : completion) {
            Integer next = counter.get(name) - 1;
            if (next == 0) counter.remove(name);
            else counter.put(name, next);
        }
        return counter.keySet().iterator().next();
    }
}