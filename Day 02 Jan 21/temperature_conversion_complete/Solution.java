
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);

        float Far = scan.nextFloat();
        double Cel = (5.0 / 9.0) * (Far - 32);
        System.out.printf("%.1f", Cel);

    }

}
