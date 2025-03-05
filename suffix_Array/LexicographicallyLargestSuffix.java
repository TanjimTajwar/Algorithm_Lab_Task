import java.util.Scanner;
import java.util.TreeSet;

public class LexicographicallyLargestSuffix {
    public static void main(String [] CSECU){
        System.out.println("Lets Code it.");

        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the String: ");
        String mystr = Arnab.next();
        
        int length = mystr.length();
        System.out.println("The Lexicographically Smallest Suffix is : "+findLSS(mystr,length));
        Arnab.close();
    }
    public static String findLSS(String mystr,int length){
        TreeSet<String> myTree = new TreeSet<>();
        for(int a=0;a<length;a++){
            myTree.add(mystr.substring(a));
        }
        return myTree.last();
    }
}


