using System;

public class Test {
    public static void Main() {
        string number;
        while((number = int.Parse(Console.ReadLine())) != 42) {
            Console.WriteLine(number);
        }
    }
}