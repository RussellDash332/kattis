import java.io.*;
import java.util.*;

class Interval implements Comparable<Interval>{
    int s;
    int e;

    Interval(int s, int e) {
        this.s = s;
        this.e = e;
    }

    @Override
    public int compareTo(Interval o) {
        if (this.e == o.e) {
            return this.s - o.s;
        }
        return this.e - o.e;
    }
}

class Pair implements Comparable<Pair>{
    int first;
    int second;

    Pair(int f, int s) {
        this.first = f;
        this.second = s;
    }

    @Override
    public int compareTo(Pair o) {
        if (this.first == o.first) {
            return this.second - o.second;
        }
        return this.first - o.first;
    }
}

public class EntertainmentBox {
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
    
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = sc.nextInt();
        int k = sc.nextInt();
        TreeSet<Pair> ts = new TreeSet<Pair>();
        List<Interval> intervals = new ArrayList<Interval>();

        while (n-- > 0)
            intervals.add(new Interval(sc.nextInt(), sc.nextInt()));
        Collections.sort(intervals);
        
        for (int i = 0; i < k; i++)
            ts.add(new Pair(0, i));

        int ans = 0;
        for (Interval interval : intervals) {
            Pair available = ts.floor(new Pair(interval.s, k));
            if (available != null) {
                int id = available.second;
                ts.remove(available);
                ts.add(new Pair(interval.e, id));
                ans++;
            }
        }

        writer.println(ans);
        writer.flush();
    }
}
