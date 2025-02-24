import java.util.Scanner;

public class Solution {

    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int factor = 3; factor * factor <= n; factor += 2) {
            if (n % factor == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean isPowerful(int n) {
        while (n % 2 == 0) {
            int power = 0;
            while (n % 2 == 0) {
                n /= 2;
                power++;
            }
            if (power == 1) {
                return false;
            }
        }

        int factor = 3;
        while (factor * factor <= n) {
            int power = 0;
            while (n % factor == 0) {
                n /= factor;
                power++;
            }
            if (power == 1) {
                return false;
            }
            factor += 2;
        }

        return n == 1;
    }

    public static int nthPowerfulNumber(int n) {
        int count = 0;
        int m = 1;

        while (count < n) {
            if (isPowerful(m)) {
                count++;
            }
            if (count < n) {
                m++;
            }
        }

        return m;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(nthPowerfulNumber(n+1));
    }
}
