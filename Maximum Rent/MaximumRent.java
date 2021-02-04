import java.io.*;
import java.util.*;

public class MaximumRent {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] line1 = sc.readLine().split(" ");
        int a = Integer.parseInt(line1[0]);
        int b = Integer.parseInt(line1[1]);
        
        String[] line2 = sc.readLine().split(" ");
        int m = Integer.parseInt(line2[0]);
        int s = Integer.parseInt(line2[1]);

        // Intersection points
        int x = s-m;
        int y = 2*m-s;

        if (s <= m+1) {
            writer.println(Math.max(Math.max(f(m-1,1,a,b),f(1,m-1,a,b)),f(1,Math.max(s-2,1),a,b)));
        } else if (s <= 2*m-1) {
            writer.println(Math.max(f(x,y,a,b),f(m-1,1,a,b)));
        } else {
            writer.println(0);
        }

        writer.flush();
    }

    public static int f(int x0, int y0, int a0, int b0) {
        return a0*x0+b0*y0;
    }
}