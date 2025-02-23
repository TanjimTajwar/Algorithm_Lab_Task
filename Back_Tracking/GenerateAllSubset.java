import java.util.*;

public class GenerateAllSubset {
   public static void main(String[] CSECU) {
       Scanner Arnab = new Scanner(System.in);
       System.out.print("Enter the number of element in the set: ");
       int a= Arnab.nextInt();
       System.out.print("Enter the elements :  ");
       int [] arr = new int[a];
       for(int b=0;b<a;b++){
        arr[b]=Arnab.nextInt();
       }
       List<List<Integer>> mylist = new ArrayList<>();
       generateSubset(arr,0,new ArrayList<>(),mylist);
       System.out.println("So the SubSet are: ");
       System.out.println(mylist);
       Arnab.close();
   }
   public static void generateSubset(int[]arr,int index,List<Integer> temp,List<List<Integer>> result){
    if(index == arr.length){
        result.add(new ArrayList<>(temp));
        return;
    }
    generateSubset(arr,index+1,temp,result);
    temp.add(arr[index]);
    generateSubset(arr,index+1,temp,result);
    temp.remove(temp.size()-1);
   }
}
