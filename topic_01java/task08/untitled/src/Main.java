import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int num;
        int sum = 0;
        int count = 0;

        num = scanner.nextInt();

        while (num != 0) {
            sum += num;
            count++;

            num = scanner.nextInt();
        }

        int average = sum / count;

        System.out.println(average);

        scanner.close();
    }
}