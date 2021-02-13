import java.io.*;
import java.util.*; // only if using sequence ADTs, like lists/maps

public class Template { // always change the name of the public class!
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        while (n--) { // one time use of n, e.g. number of test cases
            String[] line = sc.readLine().split(" ");
            int k = Integer.parseInt(line[0]);
            String p = line[1];
        }

        // code here

        writer.flush();
    }
}