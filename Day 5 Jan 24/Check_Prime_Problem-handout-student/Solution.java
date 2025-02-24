import java.util.*;

public class Solution{
    public static boolean isPrimeNumber(int num){
        if (num <= 1){
            return false;
        }

        for(int i = 2;i <= Math.sqrt(num); i++){
            if (num % i == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        boolean isPrime = isPrimeNumber(num);
        if (isPrime == false){
            System.out.println("False");
        }else{
            System.out.println("True");
        }
    }
}