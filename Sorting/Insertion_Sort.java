import java.util.Scanner;
import java.util.*;

public class Insertion_Sort {
    public static int[] arr;
    public static int num;
    public static void main(String [] CSECU){
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the Size of the Array: ");
        num = Arnab.nextInt();
        arr= new int[num];
        System.out.print("Enter the Unsorted Array: ");
        for(int a=0;a<num;a++){
            arr[a]= Arnab.nextInt();
        }
        System.out.println("Unsorted Array: "+Arrays.toString(arr));

        arr= Insertion();

        System.out.println("Sorted Array: "+Arrays.toString(arr));
    }
    public static int[] Insertion(){
        for(int a=1;a<num;a++){
            int key=arr[a];
            int b=a-1;
            while(b>=0 && arr[b]>key){
                arr[b+1]=arr[b--];
            }
            arr[b+1]=key;
        }
        return arr;
    }
}
