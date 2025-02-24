import java.util.*;

public class Solution {

    public static long calculateSquareSumOfNumbers(long n) {
        long totalSum = 0;
        for (long i = 1; i <= n; i++) {
            totalSum += i;
        }
        return totalSum * totalSum;
    }

    public static long calculateSumOfSquares(long n) {
        long totalSquareSum = 0;
        for (long i = 1; i <= n; i++) {
            totalSquareSum += i * i;
        }
        return totalSquareSum;
    }

    public static long calculateDifference(long n) {
        return calculateSquareSumOfNumbers(n) - calculateSumOfSquares(n);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        scanner.close();
        System.out.println(calculateDifference(n));
    }

}
