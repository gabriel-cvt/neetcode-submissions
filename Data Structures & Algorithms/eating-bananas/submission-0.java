class Solution {

    public int minEatingSpeed(int[] piles, int h) {

        // Descobrir maior K - criar um range entre 1 - maior K
        // Iterar por busca binária descobrindo qual o menor

        int maxK = 1;
        for (int i = 0; i < piles.length; i++) {
            if (piles[i] > maxK)
                maxK = piles[i];
        }

        int left = 1;
        int right = maxK;

        while (left < right) {
            int mid = left + (right - left) / 2;

            int temp = 0;
            for (int i =0; i < piles.length; i++) {
                temp += (piles[i] + mid - 1)/ mid;
            }

            if (temp <= h) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}
