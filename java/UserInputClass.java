
import java.util.Scanner;

public class UserInputClass {
	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);

		System.out.print("Enter something: ");

		String userInput = in.nextLine();
		
		System.out.println("You entered: " + userInput);

	}
}