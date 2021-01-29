import java.io.*;

public class TimeLoop {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int test = Integer.parseInt(sc.readLine());
        for (int i=1; i<=test; i++) {
            writer.println(i+" Abracadabra");
        }
        writer.flush();
    }
}