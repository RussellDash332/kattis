#include <bits/stdc++.h>
#define lb lower_bound
#define FOR(n) for(int i = 0; i < n; ++i)
using namespace std;

const long M = 1e9+7;
static set<long> T;
static long Z;

void add(long x) {
    auto s = T.lb(x*M+x);
    auto p = T.lb(x*M+x);
    long a = x, b = x;
    if (p != T.begin()) p--;
    if (p != T.end() && (*p)%M == x-1) {
        T.erase(p);
        Z -= ((*p)%M-(*p)/M+1)*((*p)%M-(*p)/M+1);
        a = (*p)/M;
    }
    if (s != T.end() && (*s)/M == x+1) {
        T.erase(s);
        Z -= ((*s)%M-(*s)/M+1)*((*s)%M-(*s)/M+1);
        b = (*s)%M;
    }
    T.insert(a*M+b);
    Z += (b-a+1)*(b-a+1);
}
void remove(long x) {
    auto p = T.lb(x*M+M-1);
    p--;
    T.erase(p);
    long a = (*p)/M, b = (*p)%M;
    Z -= (b-a+1)*(b-a+1);
    if (x > a) {
        Z += (x-a)*(x-a);
        T.insert(a*M+x-1);
    }
    if (x < b) {
        Z += (b-x)*(b-x);
        T.insert((x+1)*M+b);
    }
}

void init(int N, int L, int P[]) {
    FOR(N) add(P[i]);
}

void jump(int A, int B) {
    remove(A); add(B);
}

long long score() {
	return Z;
}