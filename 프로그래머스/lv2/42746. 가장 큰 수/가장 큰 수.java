import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        int len = numbers.length;
        
        String[] strings = new String[len];
        for (int i = 0; i < len; i++) {
            strings[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(strings, (s1, s2) -> -(s1 + s2).compareTo(s2 + s1));

        if (strings[0].equals("0")) return "0";
        
        return String.join("", strings);
    }
}