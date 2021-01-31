import java.io.*;

public class Skener {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] nums = sc.readLine().split(" ");
        int r = Integer.parseInt(nums[0]);
        int zr = Integer.parseInt(nums[2]);
        int zc = Integer.parseInt(nums[3]);
        for (int i = 0; i < r; i++){
            String row = sc.readLine();
            for (int k = 0; k < zr; k++) {
                for (int j = 0; j < row.length(); j++) {
                    String sub = row.substring(j,j+1);
                    for (int m = 0; m < zc; m++) {
                        writer.print(sub);
                }
            }
            writer.println();   
            }
        }
        writer.flush();
    }
}