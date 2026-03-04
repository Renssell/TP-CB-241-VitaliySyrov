public class Main {

    public static int max(int[] array) {

        int maxValue = array[0];

        for (int i = 1; i < array.length; i++) {
            if (array[i] > maxValue) {
                maxValue = array[i];
            }
        }

        return maxValue;
    }

    public static void main(String[] args) {

        int[] numbers = {3, 7, 2, 9, 5};

        int result = max(numbers);

        System.out.println(result); // 9
    }
}