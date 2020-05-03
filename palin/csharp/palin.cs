using System;

public class Palin {
	public static void Main() {
		int testCase = int.Parse(Console.ReadLine());
        for (int t = 0; t < testCase; t++) {
            int[] num = Array.ConvertAll(Console.ReadLine().ToCharArray(), elem => int.Parse(elem.ToString()));
            int n = num.Length;

            bool all9 = Array.TrueForAll(num, elem => elem == 9);
            if(all9) {
                Console.Write('1');
                for (int i = 1; i < n; i++) {
                    Console.Write('0');
                }
                Console.WriteLine('1');
            } else {
                int mid = n / 2;
                int indexOfLeftSide = mid - 1;
                int indexOfRightSide = n % 2 == 0 ? mid : mid + 1;
                
                while(indexOfLeftSide >= 0 && num[indexOfLeftSide] == num[indexOfRightSide]) {
                    indexOfLeftSide--;
                    indexOfRightSide++;
                }

                bool leftSmaller = false;
                if(indexOfLeftSide < 0 || num[indexOfLeftSide] < num[indexOfRightSide])
                    leftSmaller = true;
                
                while(indexOfLeftSide >= 0) {
                    num[indexOfRightSide] = num[indexOfLeftSide];
                    indexOfLeftSide--;
                    indexOfRightSide++;
                }

                if(leftSmaller) {
                    int carry = 1;
                    indexOfLeftSide = mid - 1;

                    if(n % 2 == 1) {
                        num[mid] += carry;
                        carry = num[mid] / 10;
                        num[mid] %= 10;
                        indexOfRightSide = mid + 1;
                    } else
                        indexOfRightSide = mid;
                    
                    while(indexOfLeftSide >= 0) {
                        num[indexOfLeftSide] += carry;
                        carry = num[indexOfLeftSide] / 10;
                        num[indexOfLeftSide] %= 10;
                        num[indexOfRightSide] = num[indexOfLeftSide];
                        indexOfLeftSide--;
                        indexOfRightSide++;
                    }
                }
                for (int i = 0; i < n; i++) {
                    Console.Write(num[i]);
                }
                Console.WriteLine();
            }
        }
	}
}