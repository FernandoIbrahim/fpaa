public class MaxMinSelection {
    public static int[] maxMinSelect(int[] arr, int start, int end) {

        if (start == end) {
            return new int[]{arr[start], arr[start]};
        }

        int mid = (start + end) / 2;

        int[] left = maxMinSelect(arr, start, mid);
        int[] right = maxMinSelect(arr, mid + 1, end);

        return findMaxMin(left, right);
    }

    public static int[] findMaxMin(int[] left, int[] right) {
        int max = Math.max(left[0], right[0]);
        int min = Math.min(left[1], right[1]);
        return new int[]{max, min};
    }

    public static void main(String[] args) {
        int[] arr = {3, 5, 1, 8, 4, 20, 2};
        int[] result = maxMinSelect(arr, 0, arr.length - 1);
        System. out.println("Max: " + result[0] + ", Min: " + result[1]);
    }

}