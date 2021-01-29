import java.io.*;
public class DetailedDifferences {
    public static void main(String[] args) throws IOException {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        int q = Integer.parseInt(sc.readLine());
        for (int i = 0;i < q;i++) {
            String a = sc.readLine();
            String b = sc.readLine();
            writer.println(a);
            writer.println(b);
            for (int j = 0; j < a.length(); j++) {
                if (a.charAt(j)==b.charAt(j)) {
                    writer.write('.');
                } else {
                    writer.write('*');
                }
            }
            writer.println();
        }
        writer.flush();
    }
}