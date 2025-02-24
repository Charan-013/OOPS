
import java.util.*;

public class Solution {

    public static void main(String[] sc) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int SurfaceArea = 2 * (a * a) + 2 * (b * b);
        System.out.printf("%d", SurfaceArea);
    }

}
