#include <iostream>
using namespace std;

int reverse(int number) {
    int remainder, reverse = 0;
    while (number != 0)
    {
        remainder = number % 10;
        reverse = reverse * 10 + remainder;
        number /= 10;
    }
    return reverse;
}

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    int n;
    cin >> n;
    for (int t = 0; t < n; t++) {
        int i, j;
        cin >> i >> j;
        int k = reverse(i) + reverse(j);
        cout << reverse(k) << endl;
    }
    return 0;
}