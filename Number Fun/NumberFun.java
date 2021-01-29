import java.io.*;

public class NumberFun {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int queries = Integer.parseInt(sc.readLine());
        for (int i=0; i<queries; i++) {
            int[] result = new int[3];
            String x = sc.readLine();
            String[] y = x.trim().split("\\s+");
            for (int j = 0; j < 3; j++) {
                result[j] = Integer.parseInt(y[j]);
            }
            int a=result[0],b=result[1],c=result[2];
            if (a+b==c) {
                writer.println("Possible");
            } else if (a-b ==c) {
                writer.println("Possible");
            } else if (b-a ==c) {
                writer.println("Possible");
            } else if (a*b == c) {
                writer.println("Possible");
            } else if (b*c == a) {
                writer.println("Possible");
            } else if (a*c == b) {
                writer.println("Possible");
            } else {
                writer.println("Impossible");
            }
        }
        writer.flush();
    }
}