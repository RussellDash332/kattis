import java.io.*;

public class R2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] nums = sc.readLine().split(" ");
        
        writer.println(2*Integer.parseInt(nums[1])-Integer.parseInt(nums[0]));
        writer.flush();
    }
}