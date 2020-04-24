#include <iostream>
#include <string>
using namespace std;

int main() {
	bool stop = false;
    for (string line; getline(cin, line);) {
    	if(line == "42")
    		stop = true;
    	if(!stop)
    		cout << line << endl;
    }
	return 0;
}