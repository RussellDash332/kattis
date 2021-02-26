#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    long double x1, y1, x2, y2, x3, y3, a, b, c, d, e, f, x, y, R, w, maxX, minX, maxY, minY, currX, currY, result;

    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }

        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

        // Find the circumcenter by radius
        a = 2*(x2-x1);
        b = 2*(y2-y1);
        c = x2*x2 + y2*y2 - x1*x1 - y1*y1;

        d = 2*(x3-x2);
        e = 2*(y3-y2);
        f = x3*x3 + y3*y3 - x2*x2 - y2*y2;

        // X and Y are the coordinates of the circumcenter, R the radius
        x = (c*e-b*f)/(a*e-b*d);
        y = (c*d-a*f)/(b*d-a*e);
        R = sqrtl((x1-x)*(x1-x)+(y1-y)*(y1-y));

        // Initial angle
        w = acosl((x1-x)/R);
        maxX = x1, maxY = y1, minX = x1, minY = x1;
        for (int i = 0; i < n; i++) { // use 0 again for double-check
            w += 2*M_PI/n;
            currX = x + R*cosl(w);
            currY = y + R*sinl(w);
            if (currX > maxX) {
                maxX = currX;
            }
            if (currX < minX) {
                minX = currX;
            }
            if (currY > maxY) {
                maxY = currY;
            }
            if (currY < minY) {
                minY = currY;
            }
        }

        // Final result
        result = (maxX-minX)*(maxY-minY);
        printf("%.10Lf\n", result);
    }

    return 0;
}