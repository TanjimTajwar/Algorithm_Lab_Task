/*
InputCopy
2
4 1
5 5 5 5
3 2
0 0 0
OutputCopy
10
0
 */
import java.util.Arrays;
import java.util.Scanner;
public class BBarrels {
    public static void main(String[] args) {
        Scanner Arnab = new Scanner(System.in);
        int t = Arnab.nextInt();
        while (t-->0) {
            int n=Arnab.nextInt();
            int k=Arnab.nextInt();
            int[] arr=new int[n];
            for (int i= 0;i<n;i++) {
                arr[i]=Arnab.nextInt();
            }
            Arrays.sort(arr);
            long result=arr[n-1];
            for (int i=n-2;i>=n-1-k;i--) {
                result +=arr[i];
            }
            System.out.println(result);
        }
        Arnab.close();
    }
}
