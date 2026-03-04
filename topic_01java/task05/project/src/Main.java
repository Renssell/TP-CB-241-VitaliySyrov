import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int h = scanner.nextInt();

        if (a >= h) {
            System.out.println(1);
        }
        else if (a <= b) {
            System.out.println("Impossible");
        }
        else {
            int remain = h - a;

            int daily = a - b;
            int days = (remain + daily - 1) / daily;

            System.out.println(days + 1);
        }

        scanner.close();
    }
}