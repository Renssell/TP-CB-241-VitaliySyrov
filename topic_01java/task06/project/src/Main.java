import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double bill = scanner.nextDouble();
        int friends = scanner.nextInt();

        if (bill < 0) {
            System.out.println("Incorrect bill");
        } else if (friends <= 0) {
            System.out.println("Incorrect number of friends");
        } else {
            double total = bill * 1.1;
            double share = total / friends;

            System.out.println(share);
        }

        scanner.close();
    }
}