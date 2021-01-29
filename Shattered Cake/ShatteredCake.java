import java.io.*;

public class ShatteredCake {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int w = Integer.parseInt(sc.readLine());
        int n = Integer.parseInt(sc.readLine());
        int area = 0;
        for (int i = 0; i < n; i++) {
            String[] nums = sc.readLine().split(" ");
            int a = Integer.parseInt(nums[0]);
            int b = Integer.parseInt(nums[1]);
            area += a*b;
        }
        writer.println(area/w);
        writer.flush();
    }
}
