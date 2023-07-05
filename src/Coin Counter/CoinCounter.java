import java.awt.*;
import java.awt.image.*;
import javax.imageio.*;

public class CoinCounter {
    public static void main(String[] args) throws Exception {
        ImageIO.setUseCache(false);
        BufferedImage img = ImageIO.read(System.in);
        byte[] pixels = ((DataBufferByte) img.getRaster().getDataBuffer()).getData();
        int[] pixels2 = new int[3000000];
        int kernelPad = 5;
        int ones = 0;
        int fives = 0;
        int tens = 0;
        int r, g, b, n;
        double x, y, y2;
        final double M1 = -0.59;
        final double N1 = 1.572;
        final double M2 = -110/3.0;
        final double N2 = 37.0;
        final double M3 = -80/3.0;
        final double N3 = 32.0;
        for (int i = 0; i < 3000000; i++) pixels2[i] = (256+pixels[i])%256;
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                n = 0;
                r = 0;
                g = 0;
                b = 0;
                for (int di = Math.max(0,i-kernelPad); di <= Math.min(999, i+kernelPad); di++) {
                    for (int dj = Math.max(0,j-kernelPad); dj <= Math.min(999, j+kernelPad); dj++) {
                        r += pixels2[3000*dj+3*di];
                        g += pixels2[3000*dj+3*di+1];
                        b += pixels2[3000*dj+3*di+2];
                        n++;
                    }
                }
                r /= n;
                g /= n;
                b /= n;
                // System.out.println(r + " " + g + " " + b);
                if (r + g + b >= 600) continue;
                x = ((double) r)/b;
                y = ((double) b)/g;
                y2 = b-g;
                if (y >= M1*x + N1) ones++;
                else if ((x <= 0.5 && y2 <= M2*x + N2) || (x > 0.5 && y2 <= M3*x + N3)) fives++;
                else tens++;
            }
        }
        long ones2;
        if (fives == 0 && tens > 100) {
            ones += 4*tens;
            ones2 = Math.round(ones/3612.5);
        } else {
            ones2 = Math.round(((double) ones + 0.014*tens)/3612.5);
            if (fives < 95000) fives -= 3600;
        }
        long fives2 = Math.round((Math.max(fives, 0) + 0.004*tens)/3544.5);
        long tens2 = Math.round(Math.round(tens - 0.0005*fives)/4105.0);
        System.out.println(ones2 + 5*fives2 + 10*tens2);
    }
}