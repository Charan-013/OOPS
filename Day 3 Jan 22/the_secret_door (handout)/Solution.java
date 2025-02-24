
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);

        boolean c1 = scan.nextBoolean();
        boolean c2 = scan.nextBoolean();
        boolean c3 = scan.nextBoolean();

        Boolean output = (c1 && c2 && c3) || (c1 && c3) || (c2 && (c1 || c3));

        if (output == true) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

    }
}
