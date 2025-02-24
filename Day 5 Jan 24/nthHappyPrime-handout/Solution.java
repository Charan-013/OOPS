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
        int maxFactor = (int) Math.sqrt(n);
        for (int factor = 3; factor <= maxFactor; factor += 2) {
            if (n % factor == 0) {
                return false;
            }
        }
        return true;
    }

    public static int sumOfSquares(int n) {
        int total = 0;
        while (n > 0) {
            int digit = n % 10;
            total += digit * digit;
            n /= 10;
        }
        return total;
    }

    public static boolean isHappy(int n) {
        boolean[] visited = new boolean[1000];
        while (n != 1) {
            if (visited[n]) {
                return false;
            }
            visited[n] = true;
            n = sumOfSquares(n);
        }
        return true;
    }

    public static boolean isHappyPrime(int n) {
        return isHappy(n) && isPrime(n);
    }

    public static int nthHappyPrime(int n) {
        int count = 0;
        int candidate = 7;
        while (count <= n) {
            if (isHappyPrime(candidate)) {
                if (count == n) {
                    return candidate;
                }
                count++;
            }
            candidate++;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(nthHappyPrime(n));
    }
}
