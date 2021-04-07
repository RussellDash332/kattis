// Using Reader class

import java.io.*;
import java.util.*;

public class AllPairsPath {
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

        int INF = 1000000000;

        while (true) {
            int n = sc.nextInt(), m = sc.nextInt(), q = sc.nextInt();
            if (n == 0 && m == 0 && q == 0) {
                writer.flush();
                return;
            }

            AdjacencyMatrix graph = new AdjacencyMatrix(n);
            while (m-- > 0)
                graph.connect(sc.nextInt(),sc.nextInt(),sc.nextInt());
            
            graph.doFloydWarshall();

            while (q-- > 0) {
                int sp = graph.D[sc.nextInt()][sc.nextInt()];
                if (sp == INF)
                    writer.println("Impossible");
                else if (sp == -INF)
                    writer.println("-Infinity");
                else
                    writer.println(sp);
            }

            writer.println();
        }
    }
}

class AdjacencyMatrix {
    public int[][] matrix;
    public int numVertices;
    public int[][] D;
    public int INF;

    public AdjacencyMatrix (int V) {
        numVertices = V;
        matrix = new int[V][V];

        INF = 1000000000;
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                matrix[i][j] = (i == j) ? 0 : INF;
    }

    public void connect (int a, int b, int w) { matrix[a][b] = Math.min(matrix[a][b], w); }

    public void doFloydWarshall () {
        D = new int[numVertices][numVertices];
        for (int i = 0; i < numVertices; i++)
            for (int j = 0; j < numVertices; j++)
                D[i][j] = matrix[i][j];

        for (int k = 0; k < numVertices; k++)
            for (int i = 0; i < numVertices; i++)
                for (int j = 0; j < numVertices; j++)
                    D[i][j] = Math.min(D[i][j], (D[i][k] == INF || D[k][j] == INF) ? INF : D[i][k]+D[k][j]);

        // Negative cycles
        for (int i = 0; i < numVertices; i++)
            for (int j = 0; j < numVertices; j++)
                for (int k = 0; k < numVertices && D[i][j] != -INF; k++)
                    if (D[i][k] != INF && D[k][j] != INF && D[k][k] < 0)
                        D[i][j] = -INF;
    }
}