
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);

        boolean soil_Dry = scan.nextBoolean();
        boolean raining = scan.nextBoolean();
        boolean day_Time = scan.nextBoolean();
        int temp = scan.nextInt();

        Boolean r = soil_Dry && (!raining) && (day_Time && (10 < temp));

        if (r == true) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}
