import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>();
        Arrays.sort(phone_book);
        for (String number : phone_book) {
            String prefix = "";
            for (char c : number.toCharArray()) {
                prefix += c;
                if (set.contains(prefix)) return false;
            }
            set.add(number);
        }
        return true;
    }
}