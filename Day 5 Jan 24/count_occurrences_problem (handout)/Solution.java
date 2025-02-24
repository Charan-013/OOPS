import java.util.Scanner;

public class Solution {

    public static int countOccurrences(String first, String second) {
        int count = 0;
        int index = 0;

        while ((index = first.indexOf(second, index)) != -1) {
            count++;
            index++;
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String first1 = sc.nextLine();
        String second1 = sc.nextLine();
        System.out.println(countOccurrences(first1, second1));
    }
}
