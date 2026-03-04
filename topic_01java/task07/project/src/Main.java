import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();
        int max = num;

        while (num != 0) {
            if (num > max) {
                max = num;
            }
            num = scanner.nextInt();
        }

        System.out.println(max);

        scanner.close();
    }
}