// Using FastIO class
import java.io.*;
import java.util.*; // only if using sequence ADTs, like lists/maps

public class Template { // always change the name of the public class!
    public static void main(String[] args) throws IOException {
        FastIO fio = new FastIO();
        
        int n = fio.nextInt();
        while (n-- > 0) { // one time use of n, e.g. number of test cases
            int k = fio.nextInt();
            String p = sc.readLine();
        }

        // code here

        fio.print("one line");
        fio.println("new line");
        fio.close();
    }
}

class FastIO extends PrintWriter { 
    BufferedReader br; 
    StringTokenizer st;

    public FastIO() { 
        super(new BufferedOutputStream(System.out)); 
        br = new BufferedReader(new InputStreamReader(System.in));
    } 

    String next() { 
        while (st == null || ! st.hasMoreElements()) { 
            try { st = new StringTokenizer(br.readLine()); } 
            catch (IOException  e) { e.printStackTrace(); } 
        } 
        return st.nextToken(); 
    } 

    int nextInt() { return Integer.parseInt(next()); } 
    long nextLong() { return Long.parseLong(next()); } 
    double nextDouble() { return Double.parseDouble(next()); } 

    String nextLine() { 
        String str = ""; 
        try { str = br.readLine(); } 
        catch (IOException e) { e.printStackTrace(); } 
        return str; 
    } 
}