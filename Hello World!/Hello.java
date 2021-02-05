import java.io.*;

public class Hello {
    public static void main(String[] args) {
        PrintWriter writer = new PrintWriter(System.out);
        writer.println("Hello World!");
        writer.flush();
    }
}
