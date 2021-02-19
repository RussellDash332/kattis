import java.io.*;
import java.util.*;

public class AlmostUnionFind {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        try {
            while (true) {
                String[] line = sc.readLine().split(" ");
                int n = Integer.parseInt(line[0]);
                int m = Integer.parseInt(line[1]);
                UFDS uf = new UFDS(n);
                int[] setCount = new int[2*n+1];
                long[] setSum = new long[2*n+1];
                for (int i = 1; i <= n; ++i) {
                    uf.ufds[i] = i+n; // we leave index 0 unused
                    uf.ufds[i+n] = i+n;
                    setCount[i+n] = 1;
                    setSum[i+n] = i;
                }

                while (m-- > 0) {
                    String[] line2 = sc.readLine().split(" ");
                    int c = Integer.parseInt(line2[0]);
                    int p = Integer.parseInt(line2[1]);
                    int q;
                    int parentP = uf.parent(p), parentQ;

                    switch (c) {
                        case 1: // merge all elements in p to q
                            q = Integer.parseInt(line2[2]);
                            parentQ = uf.parent(q);

                            if (parentP != parentQ) {
                                setCount[parentQ] += setCount[parentP];
                                setSum[parentQ] += setSum[parentP];
                                uf.ufds[parentP] = parentQ;
                            } // else do nothing, already in union
                            break;
                        case 2: // move only p to q
                            q = Integer.parseInt(line2[2]);
                            parentQ = uf.parent(q);
                            if (parentP != parentQ) {
                                setCount[parentP]--;
                                setSum[parentP] -= p;
                                setCount[parentQ]++;
                                setSum[parentQ] += p;
                                uf.ufds[p] = parentQ;
                                // no need to worry case when p is root node, since we have done path compression
                            } // else do nothing, already in same set
                            break;
                        case 3:
                            writer.print(setCount[parentP]);
                            writer.print(" ");
                            writer.println(setSum[parentP]);
                            break;
                    }

                    // writer.println(Arrays.toString(line2)+" "+Arrays.toString(uf.ufds)+" "+Arrays.toString(setCount)+" "+Arrays.toString(setSum));
                }
            }
        } catch (NullPointerException e) {
            writer.flush();
            return;
        }
    }
}

class UFDS {
    public int[] ufds;

    public UFDS (int size) {
        this.ufds = new int[2*size+1];
    }

    public int parent(int n) {
        if (this.ufds[n] == n) {
            return n;
        } else { // path compression, recursive
            return this.ufds[n] = parent(this.ufds[n]);
        }
    }
}