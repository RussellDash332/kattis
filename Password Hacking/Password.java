import java.io.*;
import java.util.Arrays;

public class Password {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        int n = Integer.parseInt(sc.readLine());
        double result = 0;
        double[] prob = new double[n];

        for (int i = 0; i < n; i++) {
            prob[i] = Double.parseDouble(sc.readLine().split(" ")[1]);
        }
        Arrays.sort(prob);
        for (int j = 1; j <= n; j++) {
            result += (n+1-j)*prob[j-1];
        }

        writer.println(result);
        writer.flush();
    }
}