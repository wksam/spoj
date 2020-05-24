#include <iostream>
#include <stack>
#include <ctype.h>
#include <string>
using namespace std;

int main() {
	int testCase = 0;
	cin >> testCase;
	for (int t = 0; t < testCase; t++){
		stack <char> s;
		string rpn = "";
		
		string expression = "";
		cin >> expression;
		
		for (char symbol : expression) {
			if (isalpha(symbol)) {
				rpn += symbol;
			} else {
				if (symbol == ')') {
					bool found = false;
					while (!found) {
						rpn += s.top() != '(' ? s.top() : '\0';
						found = s.top() == '(';
						s.pop();
					}
				} else if (symbol == '^') {
					bool stopPop = false;
					while (!stopPop) {
						if (s.top() == '+' || s.top() == '-' || s.top() == '*' || s.top() == '/' || s.top() == '^') {
							rpn += s.top();
							s.pop();
						} else {
							s.push(symbol);
							stopPop = true;
						}
					}
				} else if (symbol == '*' || symbol == '/') {
					bool stopPop = false;
					while (!stopPop) {
						if (s.top() == '+' || s.top() == '-' || s.top() == '*' || s.top() == '/') {
							rpn += s.top();
							s.pop();
						} else {
							s.push(symbol);
							stopPop = true;
						}
					}
				} else if (symbol == '+' || symbol == '-') {
					bool stopPop = false;
					while (!stopPop) {
						if (s.top() == '+' || s.top() == '-') {
							rpn += s.top();
							s.pop();
						} else {
							s.push(symbol);
							stopPop = true;
						}
					}
				} else {
					s.push(symbol);
				}
			}
		}
        cout << rpn << endl;
    }
	return 0;
}