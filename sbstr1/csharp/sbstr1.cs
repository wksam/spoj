using System;

public class Sbstr1 {
    public static void Main() {
        string input;
        while((input = Console.ReadLine()) != null) {
            string[] binaries = input.Split(' ');
            if(binaries[0].Contains(binaries[1])) Console.WriteLine(1);
            else Console.WriteLine(0);
        }
    }
}