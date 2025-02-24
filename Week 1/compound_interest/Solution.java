import java.util.*;

public class Solution{

    public static double comp_inst(int P,float R, int T){
        double ci;
        ci = P * Math.pow(1 + R/100, T) - P;
        double c = ci * 100;
        double c1 = Math.round(c);
        double c2 = c1 /100;
        return c2;
    }
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int P = scan.nextInt();
        float R = scan.nextFloat();
        int T = scan.nextInt();
        // System.out.println(P);
        // System.out.println(R);
        // System.out.println(T);
        System.out.printf("%.2f",comp_inst(P,R,T));
    }
}