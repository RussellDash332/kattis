import java.io.*;

public class ExactlyElectrical {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] nums = sc.readLine().split(" ");
        int x1 = Integer.parseInt(nums[0]);
        int y1 = Integer.parseInt(nums[1]);
        String[] nums2 = sc.readLine().split(" ");
        int x2 = Integer.parseInt(nums2[0]);
        int y2 = Integer.parseInt(nums2[1]);
        int t = Integer.parseInt(sc.readLine());
        int check = Math.abs(x2-x1)+Math.abs(y2-y1)-t;
        writer.println((check > 0 || check % 2 == 1 || check % 2 == -1) ? "N" : "Y");
        writer.flush();
    }
}