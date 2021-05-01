// Using Reader class

import java.io.*;
import java.util.*;

public class BusNumbers {
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
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return ret;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead) {
                bytesRead = din.read(buffer, bufferPointer = 0,
                                    BUFFER_SIZE);
                if (bytesRead == -1)
                    buffer[0] = -1;
            }
            return buffer[bufferPointer++];
        }
    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = sc.nextInt();
        UFDS uf = new UFDS(1001);
        while (n-- > 0) {
            int b = sc.nextInt();
            uf.insert(b);
        }

        for (int i = 1; i <= 1000; i++) {
            if (uf.p[i] == i && uf.b[i]) {
                if (uf.max[i] == uf.min[i])
                    writer.print(i+" ");
                else if (uf.max[i] - uf.min[i] == 1)
                    writer.print(uf.min[i]+" "+uf.max[i]+" ");
                else
                    writer.print(uf.min[i]+"-"+uf.max[i]+" ");
            }
        }

        writer.flush();
    }
}

class UFDS {
    public int[] p;
    public int[] min;
    public int[] max;
    public boolean[] b;
    public int[] rank;

    public UFDS(int N) {
        p = new int[N];
        min = new int[N];
        max = new int[N];
        b = new boolean[N];
        rank = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            min[i] = i;
            max[i] = i;
            b[i] = false;
            rank[i] = 0;
        }
    }

    public int findSet(int i) { 
        if (p[i] == i) return i;
        else return p[i] = findSet(p[i]); 
    }

    public void insert (int i) {
        b[i] = true;
        if (i > 0 && b[i-1])
            unionSet(i,i-1);
        if (i < 1000 && b[i+1])
            unionSet(i,i+1);
    }

    public boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) { 
        if (!isSameSet(i, j)) { 
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]) {
                p[y] = x;
                max[x] = Math.max(max[x],max[y]);
                min[x] = Math.min(min[x],min[y]);
            } else { 
                p[x] = y;
                max[y] = Math.max(max[x],max[y]);
                min[y] = Math.min(min[x],min[y]);
                if (rank[x] == rank[y])
                    rank[y]++;
            } 
        } 
    }
}