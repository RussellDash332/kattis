import java.io.*;

public class Quadrant {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int x = Integer.parseInt(sc.readLine());
        int y = Integer.parseInt(sc.readLine());

        if (x > 0 && y > 0) {
            writer.println(1);
        } else if (y > 0) {
            writer.println(2);
        } else if (x > 0) {
            writer.println(4);
        } else {
            writer.println(3);
        }

        writer.flush();
    }
}