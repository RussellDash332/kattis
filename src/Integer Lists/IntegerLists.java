import java.io.*;
import java.util.*;

public class IntegerLists {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());
        for (int i = 0; i < queries; i++) {
            String op = sc.readLine();
            int n = Integer.parseInt(sc.readLine());
            String list = sc.readLine();
            list = list.substring(1,list.length()-1);
            String[] nums = list.split(","); // the length is n
            int front = 0;
            int back = n-1;
            boolean error = false;
            int size = n;
            for (int j = 0; j < op.length(); j++) {
                switch (op.charAt(j)) {
                    case 'R':
                        int temp = front;
                        front = back;
                        back = temp;
                        break;
                    case 'D':
                        if (n > 0) {
                            if (front > back) { // the list is reversed
                                front--;
                                size--;
                            } else if (front < back) { // not reversed
                                front++;
                                size--;
                            } else if (size == 0) { // front = back, 1 element
                                error = true;
                            } else {
                                size--;
                            }
                        } else { // n = 0;
                            error = true;
                        }
                        break;
                }
            }
            if (error) {
                writer.println("error");
            } else {
                writer.print("[");
                if (n > 0) {
                    if (front > back) {
                        for (int k = front; k > back; k--) {
                            writer.print(nums[k]);
                            writer.print(",");
                        }
                    } else {
                        for (int k = front; k < back; k++) {
                            writer.print(nums[k]);
                            writer.print(",");
                        }
                    }
                    if (size != 0) {
                        writer.print(nums[back]);
                    }
                }
                writer.println("]");
            }
        }
        writer.flush();
    }
}