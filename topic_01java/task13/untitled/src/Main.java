import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static int[] removeLocalMaxima(int[] array) {

        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < array.length; i++) {

            if (i > 0 && i < array.length - 1 &&
                    array[i] > array[i - 1] &&
                    array[i] > array[i + 1]) {
                continue;
            }

            list.add(array[i]);
        }

        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }

        return result;
    }

    public static void main(String[] args) {

        int[] numbers = {18, 1, 3, 6, 7, -5};

        int[] result = removeLocalMaxima(numbers);

        System.out.println(Arrays.toString(result));
    }
}