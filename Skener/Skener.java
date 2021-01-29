import java.io.*;

public class Skener {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] nums = sc.readLine().split(" ");
        int r = Integer.parseInt(nums[0]);
        int c = Integer.parseInt(nums[1]);
        int zr = Integer.parseInt(nums[2]);
        int zc = Integer.parseInt(nums[3]);
        for (int i = 0; i < r; i++){
            String row = sc.readLine();
            String zrow = "";
            for (int j = 0; j < c; j++) {
                zrow += row.substring(j,j+1).repeat(zc);
            }
            for (int k = 0; k < zr; k++) {
                writer.println(zrow);
            }
        }
        writer.flush();
    }
}