import java.io.*;

public class Apaxiaaans {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String name = sc.readLine();
        char previous = ' ';
        for (int i = 0; i < name.length(); i++) {
            char test = name.charAt(i);
            if (!(previous == test)) {
                writer.print(test);
            }
            previous = test;
        }
        writer.flush();
    }
}