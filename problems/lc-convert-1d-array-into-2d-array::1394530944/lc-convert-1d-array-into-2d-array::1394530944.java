class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] arr = new int[m][n];
        if (original.length != m*n){
            return new int[0][0];
        }
        for(int i = 0; i < m; i++){
            int[] row = new int[n];

            for(int j = 0; j < n; j++){
                row[j] = original[i*n+j];
            }
            arr[i] = row;
        }
        return arr;
    }
}