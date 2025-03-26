import java.util.Arrays;
import java.util.Scanner;

public class Marge_Sort {
    public static int arr[];
    public static int size;
    public static void main(String [] CSECU){
        Scanner Arnab= new Scanner(System.in);
        System.out.print("Enter the Size of the Array: ");
        size= Arnab.nextInt();
        arr = new int[size];
        System.out.print("Enter the Elements of the Array: ");
        for(int a=0;a<size;a++){
            arr[a]=Arnab.nextInt();
        }

        System.out.println("Unsorted Array : "+Arrays.toString(arr));
        margeSort(0,size-1);
        System.out.println("Sorted Array   : "+Arrays.toString(arr) );
    }
    public static void margeSort(int start,int end){
        if(start<end){
            int mid= start+(end-start)/2;
            margeSort(start, mid);
            margeSort(mid+1, end);
            marge(start,end,mid);
        }
    }
    public static void marge(int s,int e,int m){
        int n1= m-s+1;
        int n2= e-m;
        int [] arr1 = new int[n1];
        int [] arr2 = new int[n2];

        for(int a=0;a<n1;a++){
            arr1[a]= arr[a+s]; 
        }
        for(int b=0;b<n2;b++){
            arr2[b]=arr[b+m+1];
        }

        int i=0,j=0,k=s;

        while(i<n1 && j<n2){
            if(arr1[i]<arr2[j]){
                arr[k++]=arr1[i++];
            }
            else{
                arr[k++]=arr2[j++];
            }
        }

        while(i<n1){
            arr[k++]=arr1[i++];
        }
        while(j<n2){
            arr[k++]=arr2[j++];
        }
    }
}
