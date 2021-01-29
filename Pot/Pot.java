import java.io.*;

public class Pot {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int queries = Integer.parseInt(sc.readLine());
        int result = 0;
        for (int i=0; i<queries; i++) {
            int n = Integer.parseInt(sc.readLine());
            result += Math.pow(n/10,n%10);
        }
        writer.println(result);
        writer.flush();
    }
}