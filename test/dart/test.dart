import 'dart:io';

void main() {
  while(true) {
    String input = stdin.readLineSync();
    if (input == "42") break;
    print(input);
  }
}