import java.util.Scanner;

class Solution {

    public static boolean isEligibleForGym(int age, double bmi, boolean health) {
        if ((age >= 18 && age <= 60) && (bmi >= 18.5 && bmi <= 24.9) && !health) {
            return true;
        } else if (age < 18 && (bmi >= 18.5 && bmi <= 24.9)) {
            return true;
        } else if ((age > 60) && (bmi >= 18.5 && bmi <= 24.9) && !health){
            return true;
        }else{
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();
        float bmi = sc.nextFloat();
        boolean health = sc.nextBoolean();

        boolean isEligible = isEligibleForGym(age, bmi, health);
        if (isEligible) {
            System.out.print("True");
        } else {
            System.out.print("False");
        }
    }
}
