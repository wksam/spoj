using System;

public class Test {
	public static void Main() {
        string line;
        bool stop = false;
        while((line = Console.ReadLine()) != null) {
            if(line == "42")
            	stop = true;
            if(!stop)
            	Console.WriteLine(line);
        }
	}
}