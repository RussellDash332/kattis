// Using Reader class

import java.io.*;
import java.util.*;

public class HauntedGraveyard {
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

        long INF = 1000000000000L;

        while (true) {
            int n = sc.nextInt(), m = sc.nextInt();
            if (n == 0 && m == 0) {
                writer.flush();
                return;
            }

            Graph graph = new Graph(n*m);

            boolean[][] graveyard = new boolean[n][m], wormhole = new boolean[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++) {
                    graveyard[i][j] = false;
                    wormhole[i][j] = false;
                }

            int g = sc.nextInt();
            while (g-- > 0)
                graveyard[sc.nextInt()][sc.nextInt()] = true;

            int h = sc.nextInt();
            while (h-- > 0) {
                int x = sc.nextInt(), y = sc.nextInt();
                graph.connect(x+y*n,sc.nextInt()+sc.nextInt()*n,sc.nextInt());
                wormhole[x][y] = true;
            }

            for (int i = 0; i < m; i++)
                for (int j = 0; j < n; j++)
                    if (!wormhole[j][i] && !graveyard[j][i] && (i != m-1 || j != n-1)) { // not the exit
                        if (j > 0 && !graveyard[j-1][i])
                            graph.connect(i*n+j,i*n+(j-1),1); // left
                        if (j < n-1 && !graveyard[j+1][i])
                            graph.connect(i*n+j,i*n+(j+1),1); // right
                        if (i > 0 && !graveyard[j][i-1])
                            graph.connect(i*n+j,(i-1)*n+j,1); // up
                        if (i < m-1 && !graveyard[j][i+1])
                            graph.connect(i*n+j,(i+1)*n+j,1); // down
                    }
            
            graph.doSSSP(0);

            long sp = graph.D[n*m-1];
            boolean never = false;
            for (int i = 0; i < n*m; i++)
                if (graph.D[i] == -INF) {
                    never = true;
                    break;
                }

            if (!never && sp == INF)
                writer.println("Impossible");
            else if (never)
                writer.println("Never");
            else
                writer.println(sp);
        }
    }
}

class Graph {
    public List<Triple> list;
    public int numVertices;
    public long[] D;
    public boolean[] neg;
    public long INF = 1000000000000L;

    public Graph (int V) {
        numVertices = V;
        list = new ArrayList<Triple>();
    }

    public void connect (int a, int b, int w) { list.add(new Triple(a,b,w)); }

    public void relax (int u, int v, int w) {
        if (D[u] != INF && D[v] > D[u] + w) // if SP can be shortened
            D[v] = D[u] + w; // relax this edge
    }

    public void doSSSP (int s) {
        // Initialize
        D = new long[numVertices];
        neg = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++) {
            D[i] = INF;
            neg[i] = false;
        }
        D[s] = 0;

        // Bellman-Ford's algorithm
        for (int i = 0; i < numVertices-1; i++)
            for (Triple edge : list)
                relax(edge.first, edge.second, edge.third);

        // Negative cycle check
        boolean stillFound = true;
        while (stillFound) {
            stillFound = false;
            for (Triple edge : list) {
                if (D[edge.first] != INF && D[edge.second] > D[edge.first] + edge.third && !neg[edge.second]) {
                    D[edge.second] = -INF; // don't use Long.MAX_VALUE nor Integer.MAX_VALUE
                    neg[edge.second] = true;
                    stillFound = true;
                }
            }
        }
    }
}

class Triple {
    public int first;
    public int second;
    public int third;

    public Triple (int a, int b, int w) {
        first = a;
        second = b;
        third = w;
    }
}