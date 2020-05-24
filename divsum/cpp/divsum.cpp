#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int testCase = 0;
	cin >> testCase;

	for (int t = 0; t < testCase; t++){
        int num = 0;
        cin >> num;
        int divsum = 0;

        for (int i = 2; i <= sqrt(num); i++) {
            if (num % i == 0)
                if (i == (num / i))
                    divsum += i;
                else
                    divsum += (i + num / i);
        }
        if(num > 1)
            divsum += 1;
        cout << divsum << endl;
    }
    return 0;
}