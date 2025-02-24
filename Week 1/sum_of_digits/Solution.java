import java.util.*;

public class Solution {

    public static long sum_of__digits(long number) {
        long sum = 0;
        while (number > 0) {
            long rem = number % 10;
            sum += rem;
            number = number / 10;
        }
        if (sum > 9){
            sum = sum_of__digits(sum);
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long number = scan.nextLong();

        System.out.println(sum_of__digits(number));
    }
}