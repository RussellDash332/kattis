import java.io.*;

public class Apaxiaaans {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String name = sc.readLine();
        String result = Character.toString(name.charAt(0));
        for (int i = 1; i < name.length(); i++) {
            char test = name.charAt(i);
            if (!(result.charAt(result.length()-1)==test)) {
                result += test;
            }
        }
        writer.println(result);
        writer.flush();
    }
}