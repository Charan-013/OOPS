import java.util.*;

public class Solution {
    public static char count_char(String word) {
        int count = 0;
        int max_count = 0;
        char ch = ' ';
        for (int i = 0; i < word.length(); i++) {
            count = 0;
            for (int j = 0; j < word.length(); j++) {
                if (word.charAt(i) == word.charAt(j)) {
                    count = count + 1;
                }
            }
            if (count > max_count) {
                max_count = count;
                ch = word.charAt(i);
            }
        }
        return ch;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String word = scan.nextLine();
        System.out.println(count_char(word));

    }
}