// Using Reader class
import java.io.*;
import java.util.*;

public class Promotions {
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
        
        int A = sc.nextInt(), B = sc.nextInt(), E = sc.nextInt(), P = sc.nextInt();
        AdjacencyList al = new AdjacencyList(E);

        for (int i = 0; i < P; i++) {
            int e1 = sc.nextInt(), e2 = sc.nextInt();
            al.connect(e1,e2);
        }

        int p1 = 0, p2 = 0, p3 = 0; // p1 = guaranteed given A promotions
                                    // p2 = guaranteed given B promotions
                                    // p3 = no chance given B promotions
        for (int i = 0; i < E; i++) {
            int d = al.DFS(i)-1, r = al.reverseDFS(i)-1;
            if (d >= E-A)
                p1++;
            if (d >= E-B)
                p2++;
            if (r >= B)
                p3++;
        }

        writer.println(p1);
        writer.println(p2);
        writer.println(p3);

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Integer>> list;
    public List<List<Integer>> rev;
    public int numVertices;
    public boolean[] visited;

    public AdjacencyList (int V) {
        numVertices = V;
        visited = new boolean[numVertices];
        list = new ArrayList<List<Integer>>();
        rev = new ArrayList<List<Integer>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Integer>());
            rev.add(new ArrayList<Integer>());
        }
    }

    public void connect (int a, int b) { // unweighted graph
        list.get(a).add(b);
        Collections.sort(list.get(a)); // O(n) just like insertion, not O(n log n)
        rev.get(b).add(a);
        Collections.sort(rev.get(b)); // O(n) just like insertion, not O(n log n)
    }

    public int DFS (int s) { // DFS from a single source
        for (int i = 0; i < numVertices; i++)
            visited[i] = false; // Initialize to 0
        return DFSRecursive(s);
    }

    public int DFSRecursive (int u) { // helper method
        // reset visited array
        visited[u] = true;
        int dfs = 1;
        for (int i = 0; i < list.get(u).size(); i++) {
            if (!visited[list.get(u).get(i)])
                dfs += DFSRecursive(list.get(u).get(i));
        }

        return dfs;
    }

    public int reverseDFS (int s) { // reverse DFS from a single source
        // reset visited array
        for (int i = 0; i < numVertices; i++)
            visited[i] = false; // Initialize to 0
        return reverseDFSRecursive(s);
    }

    public int reverseDFSRecursive (int u) { // helper method
        visited[u] = true;
        int dfs = 1;
        for (int i = 0; i < rev.get(u).size(); i++) {
            if (!visited[rev.get(u).get(i)])
                dfs += reverseDFSRecursive(rev.get(u).get(i));
        }

        return dfs;
    }
}