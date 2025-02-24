
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);

        boolean doorOpen = scan.nextBoolean();
        boolean windowOpen = scan.nextBoolean();
        boolean motionDetected = scan.nextBoolean();
        boolean alarmDeactivated = scan.nextBoolean();

        Boolean output = (doorOpen && !alarmDeactivated) || (windowOpen && !alarmDeactivated) || (motionDetected && !alarmDeactivated);

        if (output == true) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}
