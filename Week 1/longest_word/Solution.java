import java.util.*;

public class Solution {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String words = scan.nextLine();
        String word[] = words.split(" ");
        String max_Length_word = "";

        for (int i = 0; i < word.length; i++){
            if (max_Length_word.length() <= word[i].length()){
                max_Length_word = word[i];
            }
            // System.out.println(word[i]);
        }
        System.out.println(max_Length_word);
    }
}