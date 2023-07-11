import java.io.*;
import java.util.*;

public class ClosestPair2 {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 14;
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
            while (c <= ' ') { c = read(); }
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0');
            if (neg) return -ret;
            return ret;
        }

        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0');
            if (c == '.') {
                while ((c = read()) >= '0') ret += (c - '0') / (div *= 10);
            }
            if (neg) return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer=0, BUFFER_SIZE);
            if (bytesRead == -1) buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead) fillBuffer();
            return buffer[bufferPointer++];
        }
    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        Pair p1, p2, lo, hi;
        double d2;
        while (true) {
            int n = sc.nextInt();
            if (n == 0) break;
            List<Pair> pts = new ArrayList<Pair>();
            Pair[] points = new Pair[n];
            TreeSet<Pair> ts = new TreeSet<Pair>();
            while (n-- > 0) pts.add(new Pair(sc.nextDouble(), sc.nextDouble()));
            Collections.sort(pts); // use Collections' merge sort instead of Arrays' quick sort
            points = pts.toArray(points);
            Pair[] rev = new Pair[points.length];
            for (int i = 0; i < points.length; i++) rev[i] = new Pair(points[i].y, points[i].x);
            p1 = rev[0];
            p2 = points[1];
            double d = p1.distance(p2);
            int l = 0;
            for (int i = 0; i < points.length; i++) {
                while (l < i && points[i].x - points[l].x >= d) ts.remove(rev[l++]);
                lo = ts.ceiling(new Pair(points[i].y - d, -1e9));
                hi = ts.floor(new Pair(points[i].y + d, 1e9));
                if (lo != null) {
                    if (hi != null) {
                        if (lo.compareTo(hi) <= 0) {
                            for (Pair j : ts.subSet(lo, true, hi, true)) {
                                d2 = j.distance(points[i]);
                                if (d2 < d) { d = d2; p1 = j; p2 = points[i]; }
                            }
                        }
                    }
                }
                ts.add(rev[i]);
            }
            System.out.println(p1.y + " " + p1.x + " " + p2.x + " " + p2.y);
        }
    }
}

class Pair implements Comparable<Pair> {
    public double x, y;

    public Pair(double x, double y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pair o) {
        if (this.x == o.x) return this.y > o.y ? 1 : this.y < o.y ? -1 : 0;
        return this.x > o.x ? 1 : this.x < o.x ? -1 : 0;
    }

    public double distance(Pair o) {
        return Math.hypot(this.x - o.y, this.y - o.x);
    }
}