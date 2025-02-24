import java.util.*;

public class Solution{

    public static String angle_name(int angle_d){
        if (angle_d > 0 && angle_d < 90){
            return "Acute";
        }else if(angle_d == 90){
            return "Right";
        }else if(angle_d > 90 && angle_d < 180){
            return  "Obtuse";
        }else{
            return "Invalid";
        }
    }
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int angle_d = scan.nextInt();

        System.out.println(angle_name(angle_d));
    }
}