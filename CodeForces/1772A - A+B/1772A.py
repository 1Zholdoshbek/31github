import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner input = new Scanner(System.in);
	     int t = input.nextInt();
	    for(int i=0;i<t;i++){
	        String s = input.next();
	   System.out.println((s.charAt(0)-'0')+(s.charAt(2)-'0'));
	    }
	}
}