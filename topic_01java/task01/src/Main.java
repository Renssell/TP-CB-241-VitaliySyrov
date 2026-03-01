import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner example = new Scanner(System.in);

        String input = example.nextLine();

        System.out.println("Hello, " + input);

        example.close();
    }
}