import java.io.*;

public class FizzBuzz {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        String[] nums = sc.readLine().split(" ");
        int fizz = Integer.parseInt(nums[0]);
        int buzz = Integer.parseInt(nums[1]);
        int end = Integer.parseInt(nums[2]);
        for (int i = 1; i <= end; i++) {
            if (i % fizz == 0 && i % buzz == 0) {
                writer.println("FizzBuzz");
            } else if (i % fizz == 0) {
                writer.println("Fizz");
            } else if (i % buzz == 0) {
                writer.println("Buzz");
            } else {
                writer.println(i);
            }
        }
        writer.flush();
    }
}