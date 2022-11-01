import java.io.*;
import java.util.*;

public class NinetyNineProblems {
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        TreeMap<Integer, Integer> tm = new TreeMap<Integer, Integer>();
        int m = sc.nextInt(), n = sc.nextInt();
        while (m-- > 0) {
            int x = sc.nextInt();
            if (tm.get(x) == null)
                tm.put(x, 1);
            else
                tm.put(x, tm.get(x) + 1);
        }
        while (n-- > 0) {
            int q = sc.nextInt(), d = sc.nextInt();
            Integer k;
            if (q == 1)
                k = tm.higherKey(d);
            else
                k = tm.floorKey(d);
            if (k != null) {
                int f = tm.get(k);
                if (f == 1)
                    tm.remove(k);
                else
                    tm.put(k, f - 1);
            }
            writer.println(k == null ? -1 : k);
        }
        writer.flush();
    }

    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
    }
}