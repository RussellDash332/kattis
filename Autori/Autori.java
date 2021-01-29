import java.io.*;

public class Autori {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] test = sc.readLine().split("-");
        for (int i=0; i<test.length; i++) {
            writer.write(test[i].charAt(0));
            writer.flush();
        }
    }
}