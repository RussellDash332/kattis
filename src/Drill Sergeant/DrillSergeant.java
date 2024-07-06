import java.io.*;
import java.util.*;

public class DrillSergeant {
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter pw = new PrintWriter(System.out);
        int N = sc.nextInt(), M = sc.nextInt(), tmp, Q;
        long Z = 0, X = 1_000_000_001;
        long[] P = {3, 32, 323, 3233};
        Set<Long> H = new HashSet<Long>();
        TreeSet<Long> T = new TreeSet<Long>();
        while (M-- > 0) {
            int a = sc.nextInt(), b = sc.nextInt();
            if (a > b) { tmp = b; b = a; a = tmp; }
            H.add(a*X+b);
        }
        Q = sc.nextInt();
        while (Q-- > 0) {
            int c = sc.nextInt();
            long x = sc.nextInt(), z = 0;
            Long px, sx, ppx, ssx;
            if (c == 1) { T.add(x); px = T.lower(x); sx = T.higher(x); }
            else { px = T.lower(x); sx = T.higher(x); T.remove(x); }
            if (px == null && sx == null) z += 3;
            else if (px != null && sx == null) { ppx = T.lower(px); z += H.contains(px*X+x) ? ((ppx == null || !H.contains(ppx*X+px)) ? 352 : 3233) : 3; }
            else if (px == null && sx != null) { ssx = T.higher(sx); z += H.contains(x*X+sx) ? ((ssx == null || !H.contains(sx*X+ssx)) ? 352 : 3233) : 3; }
            else {
                ppx = T.lower(px); ssx = T.higher(sx);
                z -= P[(ppx != null && H.contains(ppx*X+px) ? 2 : 0)+(H.contains(px*X+sx) ? 1 : 0)];
                z -= P[(H.contains(px*X+sx) ? 2 : 0)+(ssx != null && H.contains(sx*X+ssx) ? 1 : 0)];
                z += P[(ppx != null && H.contains(ppx*X+px) ? 2 : 0)+(H.contains(px*X+x) ? 1 : 0)];
                z += P[(H.contains(x*X+sx) ? 2 : 0)+(ssx != null && H.contains(sx*X+ssx) ? 1 : 0)];
                z += P[(H.contains(px*X+x) ? 2 : 0)+(H.contains(x*X+sx) ? 1 : 0)];
            }
            Z += c == 1 ? z : -z;
            pw.println(Z);
        }
        pw.flush();
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
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return neg ? -ret : ret;
        }
        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1) buffer[0] = -1;
        }
        private byte read() throws IOException {
            if (bufferPointer == bytesRead) fillBuffer();
            return buffer[bufferPointer++];
        }
    }
}