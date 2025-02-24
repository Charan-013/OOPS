
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);
        int Age = scan.nextInt();
        boolean ID = scan.nextBoolean();
        boolean password = scan.nextBoolean();

        Boolean output = (18 <= Age && ID) || (password);

        if (output == true) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

    }
}
