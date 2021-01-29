import java.io.*;

public class Apaxiaaans {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String name = sc.readLine();
        String result = name.substring(0,1);
        for (int i = 1; i < name.length(); i++) {
            if (!result.substring(result.length()-1,result.length()).equals(name.substring(i,i+1))) {
                result += name.substring(i,i+1);
            }
        }
        writer.println(result);
        writer.flush();
    }
}