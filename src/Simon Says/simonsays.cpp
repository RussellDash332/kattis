#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    n++; // for blank line

    while (n--) {
        string word;
        getline(cin, word);
        if ((word.substr(0,10)).compare("Simon says") == 0) {
            cout << word.substr(10,word.length()) << endl;
        }
    }

    return 0;
}