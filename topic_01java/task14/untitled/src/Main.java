import java.util.Arrays;

public class Main {

    public static void cycleSwap(int[] array) {
        cycleSwap(array, 1);
    }

    public static void cycleSwap(int[] array, int shift) {

        int n = array.length;

        if (n == 0 || shift == 0) {
            return;
        }

        shift = shift % n;

        for (int s = 0; s < shift; s++) {

            int last = array[n - 1];

            for (int i = n - 1; i > 0; i--) {
                array[i] = array[i - 1];
            }

            array[0] = last;
        }
    }

    public static void main(String[] args) {

        int[] arr1 = {1, 3, 2, 7, 4};
        cycleSwap(arr1);
        System.out.println(Arrays.toString(arr1));


        int[] arr2 = {1, 3, 2, 7, 4};
        cycleSwap(arr2, 3);
        System.out.println(Arrays.toString(arr2));

    }
}