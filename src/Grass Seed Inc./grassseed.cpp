#include <iostream>
using namespace std;

int main()
{
    double c;
    int l;
    cin >> c >> l;
    double h, w;
    double ans = 0;
    while (l-- > 0) {
        cin >> h >> w;
        ans += h*w;
    }
    printf("%lf",ans*c);
    return 0;
}