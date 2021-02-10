import java.io.*;
import java.util.*; // only if using sequence ADTs, like lists/maps

public class Template {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        // frequently used formats
        int queries = Integer.parseInt(sc.readLine()); // usually the number of test cases
        String[] line = sc.readLine().split(" ");
        int n = Integer.parseInt(line[0]);

        // code here

        writer.flush();
    }
}