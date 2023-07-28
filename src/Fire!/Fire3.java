import java.io.*;
import java.util.*;

public class Fire3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] rc = sc.readLine().split(" ");
        int r = Integer.parseInt(rc[0]);
        int c = Integer.parseInt(rc[1]);

        int[][] maze = new int[r][c];

        int s=0; // Joe
        List<Integer> fires = new ArrayList<Integer>(); // Fire
        for (int i = 0; i < r; i++) {
            String row = sc.readLine();
            for (int j = 0; j < c; j++) {
                if (row.charAt(j) == '#')
                    maze[i][j] = 0;
                else {
                    maze[i][j] = 1;
                    if (row.charAt(j) == 'J')
                        s = i*c+j;
                    else if (row.charAt(j) == 'F')
                        fires.add(i*c+j);
                }
            }
        }

        AdjacencyList graph = new AdjacencyList(r*c);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (maze[i][j] == 1) {
                    if (i > 0 && maze[i-1][j] == 1)
                        graph.connect(i*c+j,(i-1)*c+j); // up
                    if (i < r-1 && maze[i+1][j] == 1)
                        graph.connect(i*c+j,(i+1)*c+j); // down
                    if (j > 0 && maze[i][j-1] == 1)
                        graph.connect(i*c+j,i*c+j-1); // left
                    if (j < c-1 && maze[i][j+1] == 1)
                        graph.connect(i*c+j,i*c+j+1); // right
                }
            }
        }

        graph.doBFS(s); // fill the J array
        graph.doBFS(fires); // fill the F array

        boolean possible = false;
        int minTime = Integer.MAX_VALUE;
        for (int i = 0; i < c; i++) {
            if (graph.J[i] != Integer.MAX_VALUE && graph.J[i] < graph.F[i]) { // top row
                minTime = Math.min(minTime, graph.J[i]);
                possible = true;
            }
            if (graph.J[(r-1)*c+i] != Integer.MAX_VALUE && graph.J[(r-1)*c+i] < graph.F[(r-1)*c+i]) { // bottom row
                minTime = Math.min(minTime, graph.J[(r-1)*c+i]);
                possible = true;
            }
        }

        for (int i = 0; i < r; i++) {
            if (graph.J[i*c] != Integer.MAX_VALUE && graph.J[i*c] < graph.F[i*c]) { // left column
                minTime = Math.min(minTime, graph.J[i*c]);
                possible = true;
            }
            if (graph.J[i*c+(c-1)] != Integer.MAX_VALUE && graph.J[i*c+(c-1)] < graph.F[i*c+(c-1)]) { // right column
                minTime = Math.min(minTime, graph.J[i*c+(c-1)]);
                possible = true;
            }
        }

        if (possible)
            writer.println(minTime+1); // extra one step to officially exit the maze
        else
            writer.println("IMPOSSIBLE");

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Integer>> list;
    public int numVertices;
    public int[] J; // for Joe
    public int[] F; // for fire
    public boolean[] visited;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Integer>>();
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Integer>());
        J = new int[numVertices]; // Initialize the J array
        F = new int[numVertices]; // Initialize the F array
        for (int i = 0; i < numVertices; i++) {
            J[i] = Integer.MAX_VALUE;
            F[i] = Integer.MAX_VALUE;
        }
    }

    public void connect (int a, int b) { list.get(a).add(b); }

    public void doBFS (int s) {
        J[s] = 0;

        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false;

        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(s);
        visited[s] = true;

        while (!q.isEmpty()) {
            Integer u = q.poll();
            for (int i = 0; i < list.get(u).size(); i++) {
                if (!visited[list.get(u).get(i)]) {
                    visited[list.get(u).get(i)] = true;
                    J[list.get(u).get(i)] = J[u] + 1;
                    q.offer(list.get(u).get(i));
                }
            }
        }
    }

    public void doBFS (List<Integer> fires) {
        Queue<Integer> q = new LinkedList<Integer>();
        for (int f : fires) {
            F[f] = 0;
            q.offer(f);
        }

        while (!q.isEmpty()) {
            Integer u = q.poll();
            for (int i = 0; i < list.get(u).size(); i++) {
                if (F[list.get(u).get(i)] > F[u] + 1) {
                    F[list.get(u).get(i)] = F[u] + 1;
                    q.offer(list.get(u).get(i));
                }
            }
        }
    }
}