import java.util.Scanner;
import java.util.TreeSet;

public class DistinctSubstrings {
    public static void main(String[] CSECU) {
        System.out.println("Aloha Bro: ");
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the String: ");
        String str= Arnab.next();
        System.out.println("Distinct Substrings Count: "+findDistinctSub(str));
        Arnab.close();
    }
    public static int findDistinctSub(String str){
        TreeSet<String> tree = new TreeSet<>();
        for(int a=0;a<str.length();a++){
            tree.add(str.substring(a));
        }

        int count=1;
        String text2=tree.first();

        for(String text: tree){
            if(text!=text2){
                count++;
            }
            text2=text;
        }
        return count;
    }
}
