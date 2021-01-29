import java.io.*;

public class SumKindOfProblem {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.readLine());
        for (int i = 0; i < n; i++) {
            String[] nums = sc.readLine().split(" ");
            int k = Integer.parseInt(nums[0]);
            int p = Integer.parseInt(nums[1]);
            writer.println(k+" "+(p*(p+1))/2+" "+p*p+" "+p*(p+1));
        }
        writer.flush();
    }
}