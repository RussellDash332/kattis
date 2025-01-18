#include <bits/stdc++.h>
#include <bitset>
#define INF INT_MAX
using namespace std;

const int BUF = 1<<15;

char inbuf[BUF]; int inpos, inlen;
char next() {
    if (inpos==inlen) {
        inpos=0; inlen=(int)fread(inbuf,1,BUF,stdin);
        if (!inlen) return EOF;
    }
    return inbuf[inpos++];
}
int read() {
    char c;
    while (!isdigit(c=next())) {}
    int x=c-48;
    while (isdigit(c=next())) x = x*10+(c-48);
    return x;
}
int read_one_digit() {
    char ch;
    while (!isdigit(ch=next())) {}
    return ch-48;
}

char outbuf[BUF], nbuf[20]; int outpos;
void flush_out() {
    fwrite(outbuf, 1, outpos, stdout); outpos = 0;
}
void wchar(char c) {
    if (outpos==BUF) flush_out();
    outbuf[outpos++] = c;
}
void write(int x) {
    int len = 0;
    for (; x>9; x/=10) nbuf[len++] = (char)(48+(x%10));
    wchar((char)(48+x));
    while (len) wchar(nbuf[--len]);
    wchar('\n');
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    assert(atexit(flush_out)==0);
    int N = read(), n = 1<<N;
    vector<vector<pair<int, int>>> G(n);
    vector<vector<int>> B(N+1);
    vector<int> R;
    for (int i = 0; i < n; i++) {
        R.push_back(bitset<32>(i).count());
        B[R[i]].push_back(i);
    }
    for (int i = 0; i < n; i++)
        for (int j = 2; j < min(N, 5); j++)
            for (int k : B[j]) G[i].push_back({i^k, 100*j*j+1});
    for (int _ = 0; _ < N<<(N-1); _++) {
        int a = read(), b = read(), w = read_one_digit();
        G[a].push_back({b, 100*w}); G[b].push_back({a, 100*w});
    }
    vector<int> D(n, INF);
    D[0] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [dd, vv] = pq.top();
        pq.pop();
        if (dd != D[vv]) continue;
        for (auto& [nn, weight] : G[vv]) {
            int newDist = dd+weight;
            if (D[nn] > newDist) {
                D[nn] = newDist;
                pq.push({newDist, nn});
            }
        }
    }
    write(D.back()/100);
    write(D.back()%100);
    return 0;
}