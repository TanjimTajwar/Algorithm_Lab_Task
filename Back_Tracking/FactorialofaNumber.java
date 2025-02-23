import java.util.Scanner;

public class FactorialofaNumber {
    public static void main(String [] CSECU){
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = Arnab.nextInt();
        System.err.println("So the Factorial of "+n+" is "+findFactorial(n));
        Arnab.close();    
    }
    public static long findFactorial(int n){
        if(n==0 || n==1){
            return 1;
        }
        return n*findFactorial(n-1);
    }
}
