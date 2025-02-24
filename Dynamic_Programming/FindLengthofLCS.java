package Dynamic_Programming;

import java.util.Scanner;

public class FindLengthofLCS {
    public static String str1;
    public static String str2;
    public static void main(String [] CSSECU){
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the 1st String: ");
        str1=Arnab.next();
        System.out.print("Enter the 2nd String: ");
        str2=Arnab.next();
        System.out.println("The length of LCS is : "+ findLengthofLCS());
        Arnab.close();
    }
    public static int findLengthofLCS(){
        int n= str1.length();
        int m= str2.length();
        int[][] dp = new int[n+1][m+1];
        for(int a=1;a<=n;a++){
            for(int b=1;b<=m;b++){
                if(str1.charAt(a-1)==str2.charAt(b-1)){
                    dp[a][b]=dp[a-1][b-1]+1;
                }
                else{
                    dp[a][b]=Math.max(dp[a-1][b], dp[a][b-1]);
                }
            }
        }
        return dp[n][m];
    }
}
