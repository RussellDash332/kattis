import java.io.*;
import java.util.*; // only if using sequence ADTs, like lists/maps

public class Template { // always change the name of the public class!
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) { // one time use of n, e.g. number of test cases
            String[] line = br.readLine().split(" ");
            int k = Integer.parseInt(line[0]);
            String p = line[1];
        }

        // code here

        writer.print();
        writer.println();
        writer.flush();
    }
}