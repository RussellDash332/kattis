import java.io.*;
import java.util.*;

public class TicketCompleted {
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = sc.nextInt(), m = sc.nextInt();
        AdjacencyList g = new AdjacencyList(n, false);
        while (m-- > 0)
            g.connect(sc.nextInt() - 1, sc.nextInt() - 1);
            
        g.colorCC();
        double res = 0;
        for (int i : g.CCSize)
            res += (double) i * (i - 1);
        writer.println(res / n / (n - 1));
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

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public boolean directed;
    public int[] visited;
    public int[] CCSize;

    public AdjacencyList (int V, boolean dir) {
        directed = dir;
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Pair>());
    }

    public void connect (int a, int b) { // unweighted graph
        connect(a, b, 1);
    }

    public void connect (int a, int b, int w) { // weighted graph
        list.get(a).add(new Pair(b,w));
        if (!directed)
            list.get(b).add(new Pair(a,w));
    }

    public List<Integer> DFSRecursive (int cc, int u) {
        visited[u] = 1;
        CCSize[cc]++;
        List<Integer> dfs = new ArrayList<Integer>();
        dfs.add(u);
        for (int i = 0; i < list.get(u).size(); i++) {
            if (visited[list.get(u).get(i).first] == 0) {
                List<Integer> dfsrec = DFSRecursive(cc, list.get(u).get(i).first);
                for (int j : dfsrec)
                    dfs.add(j);
            }
        }

        return dfs;
    }

    public void colorCC () {
        int cc = 0;
        visited = new int[numVertices];
        CCSize = new int[numVertices];

        for (int i = 0; i < numVertices; i++) {
            visited[i] = 0;
            CCSize[i] = 0;
        }

        for (int i = 0; i < numVertices; i++) {
            if (visited[i] == 0) {
                DFSRecursive(cc, i);
                cc++;
            }
        }
    }
}

class Pair implements Comparable<Pair> {
    public int first;
    public int second;

    public Pair (int v, int w) {
        first = v;
        second = w;
    }

    @Override
    public int compareTo (Pair other) {
        if (this.first != other.first)
            return this.first - other.first;
        else
            return this.second - other.second;
    }
}
