import java.io.*;

public class TrainPassengers {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        boolean result = true;
        String[] header = sc.readLine().split(" ");
        int C = Integer.parseInt(header[0]);
        int n = Integer.parseInt(header[1]);
        int inside = 0;
        for (int i=0; i<n; i++) {
            String[] flow = sc.readLine().split(" ");
            int out = Integer.parseInt(flow[0]);
            int enter = Integer.parseInt(flow[1]);
            int wait = Integer.parseInt(flow[2]);
            if (inside < out) {
                result = false;
            } else {
                inside -= out-enter; // regular flow
                /*
                Checks if :
                1. There are people waiting but the train is not full
                2. Over the capacity
                3. Last stop but there is someone waiting
                4. Negative number of passengers inside the train
                */ 
                if ((inside != C && wait > 0) || (inside > C) || (i == n-1 && wait > 0) || (inside < 0)) {
                    result = false;
                }
            }
        }
        // Checks end of train line
        if (inside != 0) {
            result = false;
        }
        writer.println(result ? "possible" : "impossible");
        writer.flush();
    }
}