import java.util.Arrays;

class Solution {
    public int heightChecker(int[] heights) {
        int j = 0;
        int length = heights.length;
        int[] results = new int[length];
        int[] expected = Arrays.copyOf(heights, length);

        Arrays.sort(expected);

        for (int i = 0; i < length; i++) {
            if (expected[i] != heights[i]) {
                results[j++] = i;
            }
        }

        // if(j==0){
        // System.out.println("All indices do not match.");
        // }else if (j==length){
        // System.out.println("All indices match.");
        // return 0;
        // }else{
        // System.out.print("Indices ");
        // for(int i=0;i<j-1;i++){
        // System.out.print(results[i]+", ");
        // }
        // System.out.print("and "+results[j-1]+ " do not match.");

        return j;
    }
}