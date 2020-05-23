using System;
using System.Collections.Generic;

public class Onp
{
	public static void Main()
	{
		int t = int.Parse(Console.ReadLine());
		for (int i = 0; i < t; i++) {
			String expression = Console.ReadLine();
			Stack<char> stack = new Stack<char>();
			String rpn = "";
			
			foreach(char symbol in expression) {
				if(Char.IsLetter(symbol)) {
					rpn += symbol;
				}
				else {
					if(symbol == ')') {
						bool found = false;
						while(!found) {
							char stackSymbol = stack.Pop();
							rpn += stackSymbol != '(' ? stackSymbol : '\0';
							found = stackSymbol == '(';
						}
					} else if(symbol == '^') {
						bool stopPop = false;
						while(!stopPop) {
							if(stack.Peek() == '+' || stack.Peek() == '-' || stack.Peek() == '*' || stack.Peek() == '/' || stack.Peek() == '^') {
								rpn += stack.Pop();
							} else {
								stack.Push(symbol);
								stopPop = true;
							}
						}
					} else if(symbol == '*' || symbol == '/') {
						bool stopPop = false;
						while(!stopPop) {
							if(stack.Peek() == '+' || stack.Peek() == '-' || stack.Peek() == '*' || stack.Peek() == '/') {
								rpn += stack.Pop();
							} else {
								stack.Push(symbol);
								stopPop = true;
							}
						}
					} else if(symbol == '+' || symbol == '-') {
						bool stopPop = false;
						while(!stopPop) {
							if(stack.Peek() == '+' || stack.Peek() == '-') {
								rpn += stack.Pop();
							} else {
								stack.Push(symbol);
								stopPop = true;
							}
						}
					} else {
						stack.Push(symbol);
					}
				}
			}
			Console.WriteLine(rpn);
		}
	}
}