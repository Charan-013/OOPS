
import java.util.*;

public class Solution {

    public static int factorial(int num) {
        int fact = 1;
        for (int i = num; i > 0; i--) {
            fact = fact * i;
        }
        return fact;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int fact = factorial(num);
        System.out.println(fact);
    }
}
