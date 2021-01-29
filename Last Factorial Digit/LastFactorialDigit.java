import java.io.*;

public class LastFactorialDigit {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int queries = Integer.parseInt(sc.readLine());
        for (int i=0; i<queries; i++) {
            int n = Integer.parseInt(sc.readLine());
            int fact = 1;
            for (int j=1; j<=n; j++) {
                fact *= j;
            }
            writer.println(fact%10);
        }
        writer.flush();
    }
}