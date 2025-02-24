
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);
        int b = scan.nextInt();
        int c = scan.nextInt();
        double root_1 = (-b + Math.sqrt((b * b) - 4 * c)) / 2;
        double root_2 = (-b - Math.sqrt((b * b) - 4 * c)) / 2;
        System.out.println(root_1);
        System.out.println(root_2);
    }
}
