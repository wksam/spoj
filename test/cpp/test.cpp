#include <iostream>
#include <string>
using namespace std;

int main() {
    for (string line; getline(cin, line);) {
    	if(line == "42") break;
    	cout << line << endl;
    }
	return 0;
}