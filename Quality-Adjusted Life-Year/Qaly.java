import java.io.*;

public class Qaly {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.readLine());
        double result = 0;
        for (int i = 0; i < n; i++) {
            String[] nums = sc.readLine().split(" ");
            result += Double.parseDouble(nums[0])*Double.parseDouble(nums[1]);
        }
        writer.println(result);
        writer.flush();
    }
}