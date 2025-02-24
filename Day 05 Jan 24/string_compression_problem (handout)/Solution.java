
import java.util.Scanner;

public class Solution {
    
    public static String compress_String(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        
        String result = "";
        int count = 1;
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                result += s.charAt(i - 1);
                if (count > 1) {
                    result += count;
                }
                count = 1;
            }
        }
        
        result += s.charAt(s.length() - 1);
        if (count > 1) {
            result += count;
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(compress_String(s)); 
    }
}
