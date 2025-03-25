import java.util.Arrays;
import java.util.Scanner;

public class Bubble_Sort {
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

        arr= Bubble();

        System.out.println("Sorted Array: "+Arrays.toString(arr));
        
    }
    public static int[] Bubble(){
        for(int a=0;a<num-1;a++){
            for(int b=a+1;b<num;b++){
                if(is_Small(a,b)){
                    int temp=arr[a];
                    arr[a]=arr[b];
                    arr[b]=temp;
                }
            }
        }
        return arr;
    }
    public static boolean is_Small(int a,int b){
        return arr[a]>arr[b];
    }
}
