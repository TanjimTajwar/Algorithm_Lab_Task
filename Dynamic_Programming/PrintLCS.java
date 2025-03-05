import java.util.Scanner;


public class PrintLCS {
    public static String str1;
    public static String str2;
    public static void main(String[] CSECU){
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the First String : ");
        str1=Arnab.next();
        
        System.out.print("Enter the Second String : ");
        str2=Arnab.next();
        Arnab.close();
        String Result= findLCS();
        System.out.print("The LCS is : "+Result+" and its length is "+ Result.length());
    }
    public static String findLCS(){
        int n= str1.length();
        int m= str2.length();
        int[][] dp= new int[n+1][m+1];
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
        StringBuilder lcs = new StringBuilder();
        while(n>0 && m>0){
            if(str1.charAt(n-1)==str2.charAt(m-1)){
                lcs.append(str1.charAt(n-1));
                n--;
                m--;
            }
            else if(dp[n-1][m]>dp[n][m-1]){
                n--;
            }
            else{
                m--;
            }
        }
        return lcs.reverse().toString();
    }
}
