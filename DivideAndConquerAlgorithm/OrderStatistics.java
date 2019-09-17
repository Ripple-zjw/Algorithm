/*
	实现第k大元素
*/

import java.util.Random;

class Solution {
    public static int findKthLargest(int[] nums, int k) {
        return quickSort(nums, 0, nums.length - 1, k);
    }

    public int quickSort(int[] nums, int left, int right, int k) {
        if (left == right) return nums[left];
        int pivot = partition(nums, left, right);
        int num = pivot - left + 1;
        if (num == k) return nums[pivot];
        else if (num > k) return quickSort(nums, left, pivot - 1, k);
        else return quickSort(nums, pivot + 1, right, k - num);
    }

    public int partition(int[] nums, int left, int right) {
        Random rand = new Random();
        int pivot = left + rand.nextInt(right - left);
        swap(nums, pivot, right);
        pivot = nums[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (nums[j] > pivot) {
                i++;
                swap(nums, i, j);
            }
        }
        swap(nums, i + 1, right);
        return i + 1;
    }

    public void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}