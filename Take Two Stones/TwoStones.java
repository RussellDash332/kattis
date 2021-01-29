import java.io.*;

public class TwoStones {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int stones = Integer.parseInt(sc.readLine());
        if (stones % 2 == 0) {
            writer.println("Bob");
        } else {
            writer.println("Alice");
        }
        writer.flush();
    }
}