
import java.util.Scanner;

public class Solution {

    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int rotateNumber(int number) {
        int length = 0;
        int temp = number;

        while (temp > 0) {
            temp = temp / 10;
            length++;
        }

        int lastDigit = number % 10;
        int rotatedNumber = number / 10;

        return lastDigit * (int) Math.pow(10, length - 1) + rotatedNumber;
    }

    public static boolean isCircularPrime(int number) {
        int rotatedNumber = number;
        int length = 0;

        while (rotatedNumber > 0) {
            rotatedNumber = rotatedNumber / 10;
            length++;
        }

        rotatedNumber = number;
        for (int i = 0; i < length; i++) {
            if (!isPrime(rotatedNumber)) {
                return false;
            }
            rotatedNumber = rotateNumber(rotatedNumber);
        }
        return true;
    }

    public static int nthCircularPrime(int n) {
        int count = 0;
        int number = 2;

        while (count < n) {
            if (isCircularPrime(number)) {
                count++;
            }
            number++;
        }
        return number - 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int result = nthCircularPrime(n);
        System.out.println(result);
    }
}
