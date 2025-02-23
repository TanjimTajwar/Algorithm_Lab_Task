import java.util.Scanner;
public class FibonacciSequence {
    public static void main(String[] CSECU) {
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the Limit of fibonacci sequence: ");
        int n = Arnab.nextInt();
        System.out.print("1+1");
        findFibonacci(n,1,1);
        Arnab.close();
    }
    public static void findFibonacci(int n,int a,int b){
        int temp=b;
        b=a+b;
        a=temp;
        if(n<a || n<b){
            return;
        }
        System.out.print("+"+b);
        findFibonacci(n, a, b);
    }
}
