import java.util.*;

public class findtheConvexHullofaSetofPoints {
    public static void main(String[] CSECU) {
        Scanner Arnab = new Scanner(System.in);
        
        System.out.print("Enter the number of points: ");
        int length = Arnab.nextInt();
        
        Point[] points = new Point[length];
        
        System.out.println("Enter the points (x y):");
        for (int a = 0; a < length; a++) {
            int b = Arnab.nextInt();
            int c = Arnab.nextInt();
            points[a] = new Point(b, c);
        }
        
        List<Point> hull = convexHull(points);
        
        System.out.println("Convex Hull: " + hull);
        
        Arnab.close();
    }

    public static List<Point> convexHull(Point[] points) {
        // Sorting the points lexicographically (by x first, then by y)
        Arrays.sort(points);

        if (points.length < 2) {
            return Arrays.asList(points);
        }

        List<Point> lower = new ArrayList<>();
        List<Point> upper = new ArrayList<>();

        // Construct the lower hull
        for (Point Q : points) { // Fixed: Used correct variable instead of an undefined 'j'
            while (lower.size() >= 2 && crossProduct(lower.get(lower.size() - 2), lower.get(lower.size() - 1), Q) <= 0) {
                lower.remove(lower.size() - 1);
            }
            lower.add(Q);
        }

        // Construct the upper hull
        for (int a = points.length - 1; a >= 0; a--) {
            Point P = points[a];
            while (upper.size() >= 2 && crossProduct(upper.get(upper.size() - 2), upper.get(upper.size() - 1), P) <= 0) {
                upper.remove(upper.size() - 1);
            }
            upper.add(P);
        }

        // Remove duplicate points (last elements of lower and upper hull are the same)
        lower.remove(lower.size() - 1); // Fixed: Ensure duplicates are removed properly
        upper.remove(upper.size() - 1);

        lower.addAll(upper);
        return lower;
    }

    // Fixed: Changed return type from 'boolean' to 'int' (cross product must return an integer)
    public static int crossProduct(Point o, Point a, Point b) {
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
    }

    static class Point implements Comparable<Point> {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Point p) {
            if (this.x == p.x) {
                return Integer.compare(this.y, p.y);
            }
            return Integer.compare(this.x, p.x);
        }

        // Fixed: Corrected string representation for proper output format
        @Override
        public String toString() {
            return "(" + x + "," + y + ")";
        }
    }
}
