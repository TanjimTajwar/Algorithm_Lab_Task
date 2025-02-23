import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 Problem 6: Palindrome Partitioning
Description: Given a string, partition it into substrings where each substring is a palindrome.
Example:
Input: "aab"
Output: [['a', 'a', 'b'], ['aa', 'b']]
 */


public class PalindromePartitioning {
    public static List<List<String>> mylist = new ArrayList<>();
    public static String str;
    public static void main(String[] args) {
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the String: ");
        str = Arnab.next();
        Arnab.close();
        findPalindromePartitioning(0,new ArrayList<>());
        System.out.println("So the Palindrome Partitioning Set is :");
        System.out.println(mylist);
    }
    public static void findPalindromePartitioning(int index,List<String> temp){
        if(index== str.length()){
            mylist.add(new ArrayList<>(temp));
            return;
        }
        for(int a=index;a<str.length();a++){
            if(isSafe(index,a)){
                temp.add(str.substring(index,a+1));
                findPalindromePartitioning(a+1,temp);
                temp.remove(temp.size()-1);
            }
        }
    }
    public static boolean isSafe(int start,int end){
        while(start<end){
            if(str.charAt(start++)!=str.charAt(end--)){
                return false;
            }
        }
        return true;
    }
    
}
