// Using Reader class

import java.io.*;
import java.util.*;

public class BST2 {
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
        
        int n = sc.nextInt();
        AVL avl = new AVL();
        int[] depth = new int[n];
        for (int i = 0; i < n; i++) {
            depth[i] = -1;
        }
        long ans = 0;

        while (n-- > 0) {
            int k = sc.nextInt();
            avl.insert(k);
            if (avl.predecessor(k) == -1 && avl.successor(k) == -1)
                depth[k-1]++;
            else if (avl.predecessor(k) == -1) // It's the smallest
                depth[k-1] = depth[avl.successor(k)-1] + 1;
            else if (avl.successor(k) == -1) // It's the largest
                depth[k-1] = depth[avl.predecessor(k)-1] + 1;
            else
                depth[k-1] = Math.max(depth[avl.successor(k)-1],depth[avl.predecessor(k)-1])+1;

            ans += depth[k-1];
            writer.println(ans);
        }

        writer.flush();
    }
}

class Vertex {
    public Vertex parent, left, right;
    public int key;
    public int height;
    public int size;

    // Constructor
    public Vertex(int v) { 
        key = v;
        parent = left = right = null;
        height = 0;
        size = 1;
    }
}

// We assume that the value of the vertices in the tree is nonnegative
class AVL {
    public Vertex root;

    public AVL() {
        root = null;
    }

    public int search(int v) {
        Vertex res = search(root, v);
        return res == null ? -1 : res.key;
    }

    // Helper method for search
    public Vertex search(Vertex T, int v) {
        if (T == null)
            return null;                // not found
        else if (T.key == v)
            return T;                   // found
        else if (T.key < v)
            return search(T.right, v);  // search to the right
        else
            return search(T.left, v);   // search to the left
    }
    
    public int findMin() {
        return findMin(root);
    }

    // Helper method for findMin
    public int findMin(Vertex T) {
        // Empty tree
        if (T == null) {
            return -1;
        }

        // Non-empty tree
        if (T.left == null)
            return T.key;               // this is the min
        else
            return findMin(T.left);     // go to the left
    }

    public int findMax() {
        return findMax(root);
    }

    // Helper method for findMax
    public int findMax(Vertex T) {
        // Empty tree
        if (T == null) {
            return -1;
        }

        // Non-empty tree
        if (T.right == null)
            return T.key;               // this is the max
        else
            return findMax(T.right);    // go to the right
    }

    public int successor(int v) {
        Vertex vPos = search(root, v);
        return vPos == null ? -1 : successor(vPos);
    }

    // Helper method for successor
    public int successor(Vertex T) {
        if (T.right != null)                    // this subtree has a right subtree
            return findMin(T.right);            // the successor is the minimum of right subtree
        else {
            Vertex par = T.parent;
            Vertex cur = T;
            // if par(ent) is not root and cur(rent) is its right children
            while ((par != null) && (cur == par.right)) {
                cur = par;                      // continue moving up
                par = cur.parent;
            }
            return par == null ? -1 : par.key;  // this is the successor of T
        }
    }

    public int predecessor(int v) {
        Vertex vPos = search(root, v);
        return vPos == null ? -1 : predecessor(vPos);
    }

    // Helper method for predecessor
    public int predecessor(Vertex T) {
        if (T.left != null)                     // this subtree has a left subtree
            return findMax(T.left);             // the successor is the maximum of left subtree
        else {
            Vertex par = T.parent;
            Vertex cur = T;
            // if par(ent) is not root and cur(rent) is its left children
            while ((par != null) && (cur == par.left)) {
                cur = par;                      // continue moving up
                par = cur.parent;
            }
            return par == null ? -1 : par.key;  // this is the predecessor of T
        }
    }

    // Added from Lecture 11: AVL Tree
    public void updateHeight(Vertex T) {
        if (T.left != null && T.right != null)
            T.height = Math.max(T.left.height,T.right.height) + 1;
        else if (T.left != null)
            T.height = T.left.height + 1;
        else if (T.right != null)
            T.height = T.right.height + 1;
        else
            T.height = 0;
    }

    // Added from Lecture 11: AVL Tree
    public void updateSize(Vertex T) {
        if (T.left != null && T.right != null)
            T.size = T.left.size + T.right.size + 1;
        else if (T.left != null)
            T.size = T.left.size + 1;
        else if (T.right != null)
            T.size = T.right.size + 1;
        else
            T.size = 1;
    }

    // Added from Lecture 11: AVL Tree
    // Balance factor of a vertex T
    public int bf(Vertex T) {
        if (T.left != null && T.right != null)
            return T.left.height - T.right.height;
        else if (T.left != null)
            return T.left.height + 1;
        else if (T.right != null)
            return -1 - T.right.height;
        else
            return 0;
    }

    public void insert(int v) {
        root = insert(root, v);
    }

    // Helper method for insert
    public Vertex insert(Vertex T, int v) {
        if (T == null)
            return new Vertex(v);           // insertion point is found

        if (T.key < v) {                    // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        }
        else {                              // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        }

        updateHeight(T);
        updateSize(T);
        T = rebalance(T);

        return T;                           // return the updated tree
    }  

    public void delete(int v) {
        root = delete(root, v);
    }

    // Helper method for delete
    public Vertex delete(Vertex T, int v) {
        if (T == null)
            return T;                                       // cannot find the item to be deleted

        if (T.key < v)                                      // search to the right
            T.right = delete(T.right, v);
        else if (T.key > v)                                 // search to the left
            T.left = delete(T.left, v);
        else {                                              // this is the node to be deleted
            if (T.left == null && T.right == null)          // this is a leaf
                T = null;                                   // simply erase this node
            else if (T.left == null && T.right != null) {   // only one child at right
                T.right.parent = T.parent;
                T = T.right;                                // bypass T
            }
            else if (T.left != null && T.right == null) {   // only one child at left
                T.left.parent = T.parent;
                T = T.left;                                 // bypass T
            }
            else {                                          // has two children, find successor
                int successorV = successor(v);
                T.key = successorV;                         // replace this key with the successor's key
                T.right = delete(T.right, successorV);      // delete the old successorV
            }
        }

        if (T != null) {
            updateHeight(T);
            updateSize(T);
            T = rebalance(T);
        }

        return T;                                           // return the updated tree
    }

    // Adapted from Lecture 11: AVL Tree
    public Vertex leftRotate(Vertex T) { // given T.right is not null
        Vertex w = T.right;
        w.parent = T.parent;
        T.parent = w;
        T.right = w.left;
        if (w.left != null)
            w.left.parent = T;
        w.left = T;

        updateHeight(T);
        updateSize(T);
        updateHeight(w);
        updateSize(w);

        return w;
    }

    // Adapted from Lecture 11: AVL Tree
    public Vertex rightRotate(Vertex T) { // given T.left is not null
        Vertex w = T.left;
        w.parent = T.parent;
        T.parent = w;
        T.left = w.right;
        if (w.right != null)
            w.right.parent = T;
        w.right = T;

        updateHeight(T);
        updateSize(T);
        updateHeight(w);
        updateSize(w);

        return w;
    }

    // Adapted from Lecture 11: AVL Tree
    public Vertex rebalance(Vertex T) {
        if (T != null) {
            if (bf(T) == 2) { // T has a left child
                if (bf(T.left) == -1) { // LR case
                    T.left = leftRotate(T.left);
                }

                // Either LL or LR case, do this
                T = rightRotate(T);
            }
            else if (bf(T) == -2) { // T has a right child
                if (bf(T.right) == 1) { // RL case
                    T.right = rightRotate(T.right);
                }

                // Either RL or RR case, do this
                T = leftRotate(T);
            }
        }

        return T;
    }
}