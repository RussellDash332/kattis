import java.io.*;

public class Carrots {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] nums = sc.readLine().split(" ");
        
        writer.println(Integer.parseInt(nums[1]));
        writer.flush();
    }
}