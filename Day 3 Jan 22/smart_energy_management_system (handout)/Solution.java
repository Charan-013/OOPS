
import java.util.Scanner;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);

        boolean houseOccupied = scan.nextBoolean();
        boolean highEnergy_appliance = scan.nextBoolean();

        boolean peakHours = scan.nextBoolean();
        int currentEnergy_usage = scan.nextInt();

        Boolean output = (!houseOccupied) || (highEnergy_appliance && peakHours) && 50 < currentEnergy_usage;

        if (output == true) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}
