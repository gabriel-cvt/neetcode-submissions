class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        return searchinMatrix(matrix, target, 0, matrix.length -1);
    }

    public boolean searchinMatrix(int[][] matrix, int target, int left, int right) {
        if (left > right) return false;
        int mid = left + (right - left) / 2;

        if (matrix[mid][0] > target) {
            return searchinMatrix(matrix, target, left, mid -1);
        }
        if (matrix[mid][matrix[mid].length -1] < target) {
            return searchinMatrix(matrix, target, mid +1, right);
        }
        return binarySearch(matrix[mid], target, 0, matrix[mid].length -1);
    }

    public boolean binarySearch(int[] arr, int target, int left, int right) {
        if (left > right) return false;
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return true;

        if (arr[mid] > target) {
            return binarySearch(arr, target, left, mid -1);
        }
        return binarySearch(arr, target, mid + 1, right);
    }
}
