import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/*
Problem 5: Subset Sum Problem
Description: Given a set of numbers and a target sum, find all subsets that sum up to the target.
Example:
Input: arr = [2, 3, 5], target = 5
Output: [[2, 3], [5]]
 */
public class SubsetSumProblem {
    public static int target;
    public static List<List<Integer>> mylist =new ArrayList<>();
    public static int n;
    public static void main(String[] CSECU) {
        Scanner Arnab = new Scanner(System.in);
        System.out.print("Enter the number of elements in the set: ");
        n= Arnab.nextInt();
        System.out.print("Enter the Set: ");
        int[] arr = new int[n];
        for(int a=0;a<n;a++){
            arr[a]=Arnab.nextInt();
        }
        System.out.print("Enter the Target Sum: ");
        target = Arnab.nextInt();
        findSubSetSum(0,new ArrayList<>(),arr,target);
        Arnab.close();
        System.out.println("So the sum set is : ");
        System.out.println(mylist);
    }
    public static void findSubSetSum(int index,List<Integer> temp,int[] arr,int remaining){
        if(remaining==0){
            mylist.add(new ArrayList<>(temp));
            return;
        }
        if(index==n || remaining<0){
            return;
        }
        temp.add(arr[index]);
        findSubSetSum(index+1,temp,arr,remaining-arr[index]);
        temp.remove(temp.size()-1);
        findSubSetSum(index+1,temp,arr,remaining);
    }
}
