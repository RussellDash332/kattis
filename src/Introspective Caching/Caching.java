import java.io.*;
import java.util.*;

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
        return o.first - this.first;
    }

    @Override
    public String toString() {
        return "[" + this.first + " " + this.second + "]";
    }
}

public class Caching {
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
        
        int c = sc.nextInt();
        int n = sc.nextInt();
        int a = sc.nextInt();

        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        boolean[] active = new boolean[n];
        List<Queue<Pair>> lqp = new ArrayList<Queue<Pair>>();
        for (int i = 0; i < n; i++) {
            lqp.add(new LinkedList<Pair>());
        }

        int[] acc = new int[a];
        for (int i = 0; i < a; i++) {
            acc[i] = sc.nextInt();
            lqp.get(acc[i]).add(new Pair(i, acc[i]));
        }

        int ans = 0;
        int numUsed = 0;
        for (int i = 0; i < a; i++) {
            if (!active[acc[i]]) {
                active[acc[i]] = true;
                ans++;
                if (numUsed < c) {
                    numUsed++;
                } else {
                    Pair evict = pq.poll();
                    active[evict.second] = false;
                }
            }
            lqp.get(acc[i]).poll();
            Pair next = lqp.get(acc[i]).peek();
            if (next == null)
                next = new Pair(a, acc[i]);
            pq.add(next);
        }

        writer.println(ans);
        writer.flush();
    }
}