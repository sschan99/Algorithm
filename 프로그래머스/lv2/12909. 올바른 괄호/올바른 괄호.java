import java.util.ArrayList;

class Solution {
    boolean solution(String s) {
        ArrayList<Character> stack = new ArrayList<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.add(c);
                continue;
            }
            if (stack.isEmpty() || stack.remove(stack.size() - 1) != '(') {
                return false;
            }
        }
        return stack.isEmpty();
    }
}