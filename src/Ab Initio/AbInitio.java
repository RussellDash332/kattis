// Using Reader class
import java.io.*;
import java.util.*;

public class AbInitio {
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int v = sc.nextInt();
        int e = sc.nextInt();
        int q = sc.nextInt();
        AdjacencyMatrix graph = new AdjacencyMatrix(v, q);

        while (e-- > 0) {
            graph.connect(sc.nextInt(), sc.nextInt());
        }

        while (q-- > 0) {
            int c = sc.nextInt();
            switch (c) {
                case 1:
                    graph.addVertex();
                    break;
                case 2:
                    graph.connect(sc.nextInt(), sc.nextInt());
                    break;
                case 3:
                    graph.clearVertex(sc.nextInt());
                    break;
                case 4:
                    graph.removeEdge(sc.nextInt(), sc.nextInt());
                    break;
                case 5:
                    graph.transpose();
                    break;
                case 6:
                    graph.complement();
                    break;
            }
        }

        int n = graph.numVertices;
        writer.println(n);
        
        for (int i = 0; i < n; i++) {
            int outDegree = 0;
            long ans = 0;
            for (int j = n-1; j >= 0; j--) {
                if (graph.transposed) {
                    if (i != j && graph.matrix[j][i] == (graph.complemented ? 0 : 1)) {
                        outDegree++;
                        ans = (7*ans + j) % 1000000007;
                    }
                } else {
                    if (i != j && graph.matrix[i][j] == (graph.complemented ? 0 : 1)) {
                        outDegree++;
                        ans = (7*ans + j) % 1000000007;
                    }
                }
            }
            writer.print(outDegree);
            writer.print(" ");
            writer.println(ans);
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
}

class AdjacencyMatrix {
    public int[][] matrix;
    public int numVertices;
    public boolean transposed;
    public boolean complemented;

    public AdjacencyMatrix (int V, int Q) { // O(V^2), construction
        numVertices = V;
        matrix = new int[V + Q][V + Q];
        transposed = false;
        complemented = false;
    }

    public void connect (int a, int b) { // O(1)
        if (transposed)
            matrix[b][a] = 1 - matrix[b][a];
        else
            matrix[a][b] = 1 - matrix[a][b];
    }

    public void transpose () { transposed = !transposed; } // O(1)
    public void complement () { complemented = !complemented; } // O(1)

    public void addVertex () { // O(V)
        if (complemented) {
            for (int i = 0; i < numVertices; i++) {
                matrix[i][numVertices] = 1;
                matrix[numVertices][i] = 1;
            }
        } else {
            for (int i = 0; i < numVertices; i++) {
                matrix[i][numVertices] = 0;
                matrix[numVertices][i] = 0;
            }
        }

        // Bottom right corner
        matrix[numVertices][numVertices] = 0;
        
        numVertices++;
    }

    public void removeEdge (int a, int b) { // O(1)
        if (transposed)
            matrix[b][a] = complemented ? 1 : 0;
        else
            matrix[a][b] = complemented ? 1 : 0;
    }

    public void clearVertex (int V) { // O(V)
        if (complemented) {
            for (int i = 0; i < numVertices; i++) {
                matrix[i][V] = 1;
                matrix[V][i] = 1;
            }
            matrix[V][V] = 0;
        } else {
            for (int i = 0; i < numVertices; i++) {
                matrix[i][V] = 0;
                matrix[V][i] = 0;
            }
        }
    }
}