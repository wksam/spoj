import java.io.*;

class Test
{
	public static void main (String[] args) throws Exception
	{
		BufferedReader r = new BufferedReader (new InputStreamReader (System.in));
		String s;
		while (!(s = r.readLine()).equals("42")) {
			System.out.println(s);
		}
	}
}