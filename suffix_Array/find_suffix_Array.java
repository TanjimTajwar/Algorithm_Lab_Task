import java.util.*;

public class find_suffix_Array {
    public static String text;
    public static void main(String[] CSECU) {
        Scanner Arnab = new Scanner(System.in);
        text = Arnab.next();
        find_suffix_array();
        Arnab.close();
    }

    public static void find_suffix_array() {
        int n = text.length();
        List<Map.Entry<Integer, String>> myList = new ArrayList<>();

        for (int a = 0; a < n; a++) {
            myList.add(new AbstractMap.SimpleEntry<>(a, text.substring(a)));
        }

        // Sort the list based on suffixes
        myList.sort(Comparator.comparing(Map.Entry::getValue));

        // Print the sorted suffix array map
        System.out.println("Suffix Array:");
        for (Map.Entry<Integer, String> answer : myList) {
            System.out.print(answer.getKey()+" ");
        }
    }
}
