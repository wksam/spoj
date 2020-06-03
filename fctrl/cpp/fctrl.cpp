#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int testCase;
    cin >> testCase;
    for (int t = 0; t < testCase; t++) {
        int n;
        cin >> n;
        int count = 0, i = 5;
        while (n / i >= 1) {
            count += n / i;
            i *= 5;
        }
        cout << count << endl;
    }
}