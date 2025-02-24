import java.util.*;

public class Solution {

    public static boolean isPalindrom(String a) {
        int length_a = a.length();

        switch (length_a) {
            case 2:
                for (int i = 0; i < a.length(); i++) {
                    for (int j = a.length() - i - 1; j > -1; j--) {
                        // System.out.println(j);
                        if (a.charAt(i) != a.charAt(j)) {
                            return false;
                        }
                    }
                }
                break;
                case 3:
                    if (a.charAt(0) != a.charAt(2)){
                        return false;
                    }
                case 4:
                    if ((a.charAt(0) != a.charAt(3)) && (a.charAt(2) != a.charAt(1))){
                        return false;
                    }
                default:
                return true;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int start = scan.nextInt();
        int stop = scan.nextInt();

        for (int i = start; i < stop; i++) {
            String a = String.valueOf(i);
            // System.out.println(a);
            if ((start < 10) && (stop <= 10)) {
                System.out.print(i + " ");
            } else if (i > 9 && isPalindrom(a)) {
                System.out.print(i + " ");

            }
        }
    }
}