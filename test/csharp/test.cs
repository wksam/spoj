using System;

public class Test {
    public static void Main() {
        string line;
        while((line = Console.ReadLine()) != null) {
            if(line == "42") break;
            Console.WriteLine(line);
        }
    }
}