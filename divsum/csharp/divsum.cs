using System;

public class DivSum
{
    public static void Main()
	{
        int testCase = int.Parse(Console.ReadLine());
        for (int t = 0; t < testCase; t++) {
            int num = int.Parse(Console.ReadLine());
            int divsum = 0;

            for (int i = 2; i <= Math.Sqrt(num); i++) {
                if (num % i == 0) {
                    if (i == (num / i))
                        divsum += i;
                    else
                        divsum += (i + num / i);
                }
            }
            if (num > 1)
                divsum += 1;
            Console.WriteLine(divsum);
        }
    }
}