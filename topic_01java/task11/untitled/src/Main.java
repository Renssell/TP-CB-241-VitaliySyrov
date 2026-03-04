public class Main {

    public static int sum(int[] array) {

        if (array == null || array.length == 0) {
            return 0;
        }

        int total = 0;

        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 0) {
                total += array[i];
            }
        }

        return total;
    }

    public static void main(String[] args) {

        int[] numbers = {1, 2, 3, 4, 5, 6};

        int result = sum(numbers);

        System.out.println(result);
    }
}